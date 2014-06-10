import sys
import os
from subprocess import call

def main(argv):
	directory = argv[0]
	onlyfiles = [ f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory,f)) ]
	for file in onlyfiles:
		filename, ext = os.path.splitext(file)
		#print filename + "-7.1.1" + ext
		xml = os.path.join(directory,filename + ".xml")
		dirname = os.path.dirname(os.path.realpath(__file__))
		executable = os.path.join(dirname,"cutdetect")
		call([executable,"-nokeyframes",os.path.join(directory,file), xml])

if __name__ == "__main__":
   main(sys.argv[1:])
