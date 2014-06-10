import sys
import os

def main(argv):
	directory = argv[0]
	version = argv[1]
	onlyfiles = [ f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory,f)) ]
	for file in onlyfiles:
		filename, ext = os.path.splitext(file)
		os.rename(os.path.join(directory,file), os.path.join(directory,filename + "-" + version + ext))

if __name__ == "__main__":
   main(sys.argv[1:])