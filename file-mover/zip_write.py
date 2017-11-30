import zipfile, os
os.chdir('C:\\Users\\AlexDeepDive\\Documents\\DEV\\python-sys-jobs\\file-mover')
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('dd_pic_1.png', compress_type=zipfile.ZIP_DEFLATED)
newZip.write('dd_pic_2.png', compress_type=zipfile.ZIP_DEFLATED)
newZip.write('test.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.write('how_to_avoid_analysis_paralysis.PNG', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()