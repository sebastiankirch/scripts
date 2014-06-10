from xlrd import open_workbook
from xlwt import Workbook
from xlwt import easyxf
from xlutils.copy import copy
import sys, getopt, shutil
from os import rename
from os import listdir
from os.path import isfile, join, exists, split,splitext

def main(argv):
    try:
       opts, args = getopt.getopt(argv,"hs:")
    except getopt.GetoptError:
       print sys.argv[0] + ' -s <source_directory>'
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
          print sys.argv[0] + ' -s <source_directory>'
          sys.exit()
       elif opt in ("-s"):
          source_directory = arg
    
    # add all the files in 'source_directory' to a list
    onlyfiles = [ f for f in listdir(source_directory) if isfile(join(source_directory,f)) ]
    
    workbook = Workbook() 
    sheet = workbook.add_sheet("Sheet Name") 
    index = 1
    for file in onlyfiles:
        head, tail = split(file)
        sheet.write(index,0,tail)
        sheet.write(index,1,splitext(tail)[0])
        index += 1
       
    workbook.save('result.xls')
    
if __name__ == "__main__":
   main(sys.argv[1:])



