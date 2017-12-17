#! python3
# errorExample.py

def spam():
    bacon()
def bacon():
    raise Exception ('this is an error...')

spam()
