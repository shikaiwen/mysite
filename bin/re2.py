import os

for filename in os.listdir("."):
   # os.rename(old_file_name, new_file_name) 
	#print(filename)
	if " " in filename:
		new_filename = filename.replace(" ","")
		os.rename(filename, new_filename) 
		#print(filename)
