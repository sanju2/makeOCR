'''
    Author: Pesi, pesi_taototo@outlook.com
    
    Description: This is a script that is meant to interact with
    a Tesseract-OCR build on Windows.
    
    The input is expected to be JPG, JPEG, PNG, or TIFF images
    that is drag n' drop by the user, then it will pass each
    images to Tesseract to get the textual output.
    
'''

from os import path
from sys import argv 
import subprocess

tesseract_folder="C:\\Program Files (x86)\\Tesseract-OCR\\"
tesseract_exe="tesseract.exe"
# check if Tesseract-OCR exist in Program Files (x86) directory
T_exists = path.isdir(tesseract_folder)

if T_exists:
    argc=len(argv)
   
    for i in range(1, argc):
        output = path.splitext(argv[i])[0]
        output = output+".txt"
                
        # - > is necessary because Tesseract line feeds at EOL rather than carriage returns + line feed
        # necessary for Unix -> Windows conversion, we redirect the output to a file
        #subprocess.call([tesseract_exe, argv[i], -, >, output])
        subprocess.Popen(tesseract_exe + " " + argv[i] + " - >" + output, cwd='C:\\Program Files (x86)\\Tesseract-OCR\\', shell=True)

else:
    print("ERROR: Tesseract-OCR folder does not exist in Program Files (x86)")
    input("Press RETURN to quit>>") # hangs the script until user input so the error can display