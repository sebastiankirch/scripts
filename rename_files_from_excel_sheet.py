from xlrd import open_workbook
from xlwt import Workbook
from xlwt import easyxf
from xlutils.copy import copy
import sys, getopt, shutil
from os import rename
from os import listdir
from os.path import isfile, join, exists, split

def main(argv):
    try:
       opts, args = getopt.getopt(argv,"hi:s:t:")
    except getopt.GetoptError:
       print sys.argv[0] + ' -i <inputfile> -s <source_directory> -t <target_directory>'
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
          print sys.argv[0] + ' -i <inputfile> -s <source_directory> -t <target_directory>'
          sys.exit()
       elif opt in ("-i"):
          inputfile = arg
       elif opt in ("-s"):
          source_directory = arg
       elif opt in ("-t"):
          target_directory = arg
    
    # add all the files in 'source_directory' to a list
    onlyfiles = [ f for f in listdir(source_directory) if isfile(join(source_directory,f)) ]
    
    # open the input Excel file
    wb = open_workbook(inputfile)
    sheet = wb.sheet_by_index(0)
    book = copy(wb)
    csheet = book.get_sheet(0)

    index = 1
    for row in range(sheet.nrows):
        source_filename = sheet.cell(row,2).value[:-3] + 'pdf'
        
        if source_filename in onlyfiles:
            source_file = join(source_directory, source_filename)
            target_file = ''
            target_filename = ''
            
            ordner = sheet.cell(row,0).value
            if isinstance(ordner, float):
                ordner = str(ordner)
            ordner = ordner.strip().replace('\\','_').replace('/','_').replace(':','_').replace('*','_').replace('?','_').replace('\"','_').replace('<','_').replace('>','_').replace('|','_')
                
            register = sheet.cell(row,1).value
            print register
            if isinstance(register, float):
                register = str(register)
            register = register.strip().replace('\\','_').replace('/','_').replace(':','_').replace('*','_').replace('?','_').replace('\"','_').replace('<','_').replace('>','_').replace('|','_')
            
            # use 'ordner' as filename
            # remove invalid characters
            target_filename = ordner
                   
            if len(register) != 0:     
                if len(target_filename + '_' + register) > 200:
                    target_filename = target_filename[:(200-len(register))]
                                
                target_filename += '_' + register
            else:
                if len(target_filename) > 200:
                    target_filename = target_filename[:200]
            
            print target_filename
            
            # create target path
            target_file = join(target_directory, target_filename)
            # if the filename is not unique, append a number
            if exists(target_file + '.pdf'):
                i = 1
                while True:
                    if exists(target_file + '_' + str(i) + '.pdf'):
                        i += 1
                    else: 
                        target_file = target_file + '_' + str(i)
                        break
            target_file = target_file + '.pdf'
            
            print source_file + '[' + str(index) +  '/' + str(len(onlyfiles) - 1) + ']'
            head, tail = split(target_file)
            csheet.write(row,8,tail)
            if not exists(target_file):
                shutil.copy(source_file, target_file)
            index += 1
       
    book.save('result.xls')
    
if __name__ == "__main__":
   main(sys.argv[1:])



