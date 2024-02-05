import os

path = "/gdrive/MyDrive/Angel"#@param{type:"string"}
file_type = 'mkv' #@param ["mkv", "mp4"]

my_list = []

for (root, dirs, file) in os.walk(path):
	for f in file:
		if '.file_type' in f:
			print(path+"/"+f)
		my_list.append(path+"/"+f)

print(my_list)

a = 0

while a < len(my_list):
  vf = my_list[a]

  !ffmpeg -i "$vf"

  a = a + 1
