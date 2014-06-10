import csv
import codecs
import sys, shutil
from os import rename
from os import listdir
from os.path import isfile, join, exists, split, splitext
from xml.dom import minidom

def main(argv):
    input = argv[0]
    list = argv[2]
    output = argv[1]

    onlyfiles = [ join(input,f) for f in listdir(input) if isfile(join(input,f)) ]

    for f in onlyfiles:

        path, file = split(f)
        filename, ext = splitext(file)

        with open(list, "rb") as csvfile:
            listreader = csv.reader(csvfile, delimiter=';')
            for row in listreader:
                unicode_row = [x.decode('utf-8') for x in row]
                if row[0] == filename:
                    title = unicode_row[1]

        with codecs.open(f, "r", "utf-8") as inp:
            xmldoc = minidom.parseString(inp.read().encode("utf-8"))

        itemlist = xmldoc.getElementsByTagName('ns1:Title')

        itemlist[0].firstChild.data = title

        with codecs.open(join(output, file), "w", "utf-8") as f:
            xmldoc.writexml(f)

if __name__ == '__main__':
    main(sys.argv[1:])
