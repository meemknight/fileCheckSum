import sys
import os
from hashFunc import *
import shelve

assertionTool(len(sys.argv) > 1 and sys.argv[1] != "", "Usage: py calculateSum <folder path>")


path = sys.argv[1]

assertionTool(os.path.isdir(path), "please specify a valid directory")

sh = shelve.open(path)
sh.clear()

for folderName, subFolders, files in os.walk(path):
    for i in files: 

        currentFullFileName = os.path.join(folderName, i)
        currentShortFileName = currentFullFileName[len(path)+1:]
        f = open(currentFullFileName)
        fileContent = f.read()
        h = hashFunc(fileContent)
        sh[currentShortFileName] = h
        print(f"{currentShortFileName} : {h}")
        f.close()

if len(sh) == 0:
    print("No files found in the directory.")

sh.close()