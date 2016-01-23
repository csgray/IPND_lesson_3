# Lesson 3.2: Use Functions
# Mini-Project: Secret Message

# Your friend has hidden your keys! To find out where they are,
# you have to remove all numbers from the files in a folder
# called prank. But this will be so tedious to do!
# Get Python to do it for you!

# Use this space to describe your approach to the problem.
# Step 1: Convert file name to string
# Step 2: Replace number characters with ""
# Step 3: Rename file with new string

import os

def rename_files():
	file_list = os.listdir("/home/corey/code/lesson_3/prank")
	saved_path = os.getcwd()
	os.chdir("/home/corey/code/lesson_3/prank")
	# 
	for file_name in file_list:
		print("Old Name - " + file_name)
		print("New Name - " + file_name.translate(None, "0123456789"))
		os.rename(file_name, file_name.translate(None, "0123456789"))
	os.chdir(saved_path)

rename_files()