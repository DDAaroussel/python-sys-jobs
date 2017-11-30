import zipfile, os
os.chdir('C:\\Users/AlexDeepDive/Documents/DEV/python-sys-jobs/file-mover')    # move to the folder with example.zip
exampleZip = zipfile.ZipFile('alex_roussel_CV.zip')
exampleZip.extractall()
exampleZip.close()