# makeOCR
A simple python script for OCR processing using open source tool tesseract.

## What's special about this?
Nothing. This script just accepts a drag n' drop png, jpg, jpeg, tiff image file, runs it in a background shell and the open source Tesseract-OCR tool will generate a text file, corresponding to the same filename of the image file, in the directory of the image file.

## Specification
The source code for this is located in ./source. We merely use $ pyinstaller makeOCR.py to generate the makeOCR.exe executable.

## Installation
### Prerequisite
You must first get a copy of Tesserect-OCR from UB Manheim here: https://github.com/UB-Mannheim/tesseract/wiki. 
You must store the Tesseract-OCR folder in C:\Program Files (x86)\ for the script to work.

### Installing makeOCR
To install makeOCR, 
1. download the zip file of this project.
2. Extract the contents of the zip file to any location you desire
3. Create a desktop shortcut linking to makeOCR.exe in the location in step 2

### Using makeOCR
Using makeOCR is simple. After creating a desktop shortcut to the executable described in step 3 of Installing makeOCR, simply drag and drop an image to the desktop shortcut and the image will be processed in the background.

makeOCR can more than one multiple drag n' drop image file.
