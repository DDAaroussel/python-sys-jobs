#treeWalk script
import os

for folderName, subfolders, filenames in os.walk('D:\\DEV'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')

#code to execute the script:
#exec(open("./delete.py").read())
