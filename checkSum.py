import sys
import os
from hashFunc import *
import shelve

assertionTool(len(sys.argv) > 1 and sys.argv[1] != "", "Usage: py checkSum <folder path>")

path = sys.argv[1]

assertionTool(os.path.isdir(path), "please specify a valid directory")

sh = shelve.open(path)

assertionTool(len(sh) != 0, "the sum was not calculated before")

readFolders = dict()

for folderName, subFolders, files in os.walk(path):
    for i in files: 

        currentFullFileName = os.path.join(folderName, i)
        currentShortFileName = currentFullFileName[len(path)+1:]
        f = open(currentFullFileName)
        fileContent = f.read()
        h = hashFunc(fileContent)
        readFolders[currentShortFileName] = h
        f.close()

for k, v in sh.items():
    if k not in readFolders:
        print("a file was removed:", k)
    else:
        if v != readFolders[k]:
            print("file corupted:", k)
        else:
            print("file ok:", k)
    del readFolders[k]

for k, v in readFolders.items():
    print("A new file was added:", k)