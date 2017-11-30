import shutil, os
os.chdir('D:\\DEV/python-sys-jobs/file-mover')
for filename in os.listdir():
    if filename.endswith('.txt'):
        os.unlink(filename)
        print(filename)
		
#code to execute the script:
#exec(open("./delete.py").read())