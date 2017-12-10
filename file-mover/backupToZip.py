#! python3
# backupToZip.py - Copies an entire folder and contents into
# ZIP file backup.

import zipfile, os

#folder = 'D:\\DEV/python-sys-jobs/file-mover'

# 'file-mover' is an example value for folder. abspath() will return the
# whole file path without you needing to enter it.

def backupToZip(folder):

    folder = os.path.abspath(folder)

    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '_' + '.zip'
        if not os.path.exists(zipFileName):
            break
        number = number + 1

    #Create the ZIP file
    print('Creating %s...' % (zipFileName))
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    # Walk the directory tree backing up folders.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        #Add folder to zip file
        backupZip.write(foldername)
        #Add all files in this folder to the zip file
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue #don't backup the backup zip files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')

backupToZip('./')
