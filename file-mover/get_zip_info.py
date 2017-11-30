import shutil, os, zipfile
os.chdir('C:\\Users/AlexDeepDive/Documents/DEV/python-sys-jobs/file-mover/rjokes.zip')
exampleZip = zipfile.ZipFile('alex_roussel_CV.zip')
exampleZip.namelist()
file_one = exampleZip.getinfo('1.png')
file_one.file_size
file_one.compress_size
'Compressed file is %sx smaller!' % (round(file_one.file_size / file_one.compress_size, 2))
exampleZip.close()
