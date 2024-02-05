import os, sys, re

# This is my path
path = "Enter video folder path"#@param {type:"string"}
resolution = 'enter desired video resolution' #@param ["2160p", "1440p", "1080p", "720p", "480p", "360p", "240p"]
file_type = 'enter file type' #@param ["mkv", "mp4"]

my_list = []

# dirs=directories
for (root, dirs, file) in os.walk(path):
	for f in file:
		if '.file_type' in f:
			print(path+"/"+f)
		my_list.append(path+"/"+f)

print(my_list)

a = 0

while a < len(my_list):
	vf = my_list[a]

	delsplit = re.search("\/(?:.(?!\/))+$", vf)
	testsplit = vf.split("/")
	filename = re.sub("^[\/]", "", delsplit.group(0))
	filename_raw = re.sub(".{4}$", "", filename)
	resolution_raw = re.search("[^p]{3,4}", resolution)
	of = re.search("^[\/].+\/", vf)

	os.environ['inputFile'] = vf
	os.environ['outputPath'] = of.group(0)
	os.environ['fileName'] = filename_raw
	os.environ['fileType'] = file_type
	os.environ['resolutionHeight'] = resolution_raw.group(0)

	!ffmpeg -hide_banner -i "$inputFile" -c:v hevc -vf "scale=-1:"$resolutionHeight"" -b:v 512k -c:a aac -b:a 128k -strict experimental -sn "$outputPath"/"$fileName"-"$resolutionHeight"p."$fileType"

	!ffmpeg -hide_banner -i "$inputFile" -c:s copy "$outputPath"/"$fileName".ass

	!ffmpeg -hide_banner -i "$outputPath"/"$fileName".ass -c:s srt "$outputPath"/"$fileName".srt

	!ffmpeg -hide_banner -i "$outputPath"/"$fileName"-"$resolutionHeight"p."$fileType" -i "$outputPath"/"$fileName".srt -c copy -c:s srt "$outputPath"/"$fileName"-subbed.mkv

	a = a + 1
