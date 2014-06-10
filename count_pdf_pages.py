from xlrd import open_workbook
from xlwt import Workbook
from xlwt import easyxf
from xlutils.copy import copy
import sys, getopt, shutil
from os import rename
from os import listdir
from os.path import isfile, join, exists, split
from pyPdf import PdfFileWriter, PdfFileReader

def main(argv):
    try:
       opts, args = getopt.getopt(argv,"hi:s:")
    except getopt.GetoptError:
       print sys.argv[0] + ' -i <inputfile> -s <source_directory>'
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
          print sys.argv[0] + ' -i <inputfile> -s <source_directory>'
          sys.exit()
       elif opt in ("-i"):
          inputfile = arg
       elif opt in ("-s"):
          source_directory = arg
    
    # add all the files in 'source_directory' to a list
    #onlyfiles = [ f for f in listdir(source_directory) if isfile(join(source_directory,f)) ]
    
    # open the input Excel file
    wb = open_workbook(inputfile)
    sheet = wb.sheet_by_index(0)
    book = copy(wb)
    csheet = book.get_sheet(0)

    index = 1
    for row in range(sheet.nrows):
        source_filename = sheet.cell(row,0).value
        
        #if source_filename in onlyfiles:
        source_file = join(source_directory, source_filename)
            
        input1 = PdfFileReader(file(source_file, "rb"))
        numPages = input1.getNumPages()
        print str(index) + " " + str(numPages)
        csheet.write(row,11,numPages)
        index += 1
            
    book.save('result.xls')
    
if __name__ == "__main__":
   main(sys.argv[1:])



