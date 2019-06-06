'''
    author: pesi 
    email: pesiii@outlook.com
    date: June 6, 2019
    
    Description: This is a script that is meant to interact with
    a Tesseract-OCR build on Windows.
    
    The input is expected to be JPG, JPEG, PNG, or TIFF images
    that is drag n' drop by the user, then it will pass each
    images to Tesseract to get the textual output.
    
'''

from os import path
from sys import argv 
import subprocess

tesseract_filepath="C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

# check if Tesseract-OCR exist in Program Files (x86) directory
T_exists = path.isfile(tesseract_filepath)

if T_exists:
    argc=len(argv)
   
    for i in range(1, argc):
        output = path.splitext(argv[i])[0]
        subprocess.call([tesseract_filepath, argv[i], output])
       

else:
    print("ERROR: Tesseract-OCR folder does not exist in Program Files (x86)")
    input("Press RETURN to quit>>") # hangs the script until user input so the error can display