# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 17:16:37 2020

@author: reach
"""

import PyPDF2, os

pdfFiles = []
for filename in os.listdir('.'):
    pdfFiles.append(filename)
pdfFiles.sort(key = str.lower)

pdfWriter = PyPDF2.PdfFileWriter()


for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
for pageNum in range(1, pdfReader.numpages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
    
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()