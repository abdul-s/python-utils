#/bin/python
import glob
from os import path 
import os

code_path = "/home/my_project"
ext_list = ["*.js","*.html","*.sql"]
skip_list = ["node_modules","assets","js"]

def get_all_file_wrapper(ext=ext_list, base_path=code_path, file_list=[]):
	for ext in ext_list:
		files = glob.glob( path.join(base_path,ext) )
		if len(files) > 0:
			file_list.extend(files)
		file_list.extend(get_all_file(ext,base_path,[]))
	return file_list

def get_all_file(ext, base_path, file_list):
	try:
		list_dir = os.listdir(base_path)
	except:
		return
	for dir in list_dir:
		if dir in skip_list:
			continue 
		files = glob.glob( path.join(base_path,dir,ext) )
		if len(files) > 0:
			file_list.extend(files)
		get_all_file(ext,path.join(base_path,dir),file_list)
	return file_list

all_file = get_all_file_wrapper()
all_file.sort()
total_count = 0
for file in all_file:
	line_count = 0
	with open(file,'r') as f:
		for line in f:
			if len(line) > 0 and line != '\n':
				line_count += 1
		print file,":::",line_count
	total_count += line_count

print "Count:::",total_count
