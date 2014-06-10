from xlrd import open_workbook
from xlwt import Workbook
from xlwt import easyxf
from xlutils.copy import copy
import sys, getopt
from os import listdir
from os.path import isfile, join

def main(argv):
    try:
       opts, args = getopt.getopt(argv,"hi:d:")
    except getopt.GetoptError:
       print sys.argv[0] + ' -i <inputfile> -d <directory>'
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
          print sys.argv[0] + ' -i <inputfile> -d <directory>'
          sys.exit()
       elif opt in ("-i"):
          inputfile = arg
       elif opt in ("-d"):
          directory = arg
    onlyfiles = [ f for f in listdir(directory) if isfile(join(directory,f)) ]
    
    wb = open_workbook(inputfile)

    sheet = wb.sheet_by_index(0)

    book = copy(wb)
    csheet = book.get_sheet(0)
    
    for row in range(sheet.nrows):
        v = sheet.cell(row,1).value
        if isinstance(v, float):
            v = int(v)
        name = str(v) + '.pdf'
        check = name in onlyfiles;
        if check:
            csheet.write(row,0,'1')
            
    book.save('result.xls')

if __name__ == "__main__":
   main(sys.argv[1:])



