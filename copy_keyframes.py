import click
import shutil
from os import rename
from os import listdir
from os.path import isfile, join, exists, split

# 
# @author skirch
#
# options
#   -o / --output   output directory
#
# arguments
#   [1] directory to be processed
# 
@click.command()
@click.option('-o','--output', default=False, help='output directory')
@click.argument('input')
def copyKeyframes(input, output):
    directories = [ join(input,d) for d in listdir(input)  ]
    for directory in directories:
    	print(directory)
    	keyframes = [ join(directory,f) for f in listdir(directory)  ]
    	head, tail = split(directory)
    	
    	shutil.copy(keyframes[0], join(output, tail + ".jpg"))
    	
if __name__ == '__main__':
    copyKeyframes()