import os
import sys

def main(argv):
    if len(argv) > 0:
        os.chdir(argv[0])
    
    f = open('filelist.txt', 'w')
    for file in os.listdir("."):
        if file != 'filelist.txt':
            f.write(file + '\n')
    
if __name__ == "__main__":
   main(sys.argv[1:])
