import os 
import shutil
def swapFileData():
	source = input("enter source folder name: ")
	destination = input("enter the destination folder name: ")

	source = source + "/"
	destination = destination + "/"
	list_of_files = os.listdir(source)
	for file in list_of_files: 
    		shutil.copy((source+ file), destination)
