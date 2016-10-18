# -*- coding=utf-8 -*-
#author: karezi
#2016-10-18 13:23
"""
Usage:
Download PDFs from CVF Open Access
Support:
Python3
"""
import urllib.request
import re
import os
import sys

conference = "CVPR2016"
rootUrl = "http://www.cv-foundation.org/openaccess/"
pageUrl = rootUrl + conference + ".py"
outputDirPath = "./" + conference + "/"
html = bytes.decode(urllib.request.urlopen(pageUrl).read())
pdfUrls = re.findall(r'<a href=(.*?).pdf">pdf</a>', html)
pdfUrl_sum = len(pdfUrls)
if not os.path.exists(outputDirPath):
	os.mkdir(outputDirPath)
for i, element in enumerate(pdfUrls):
    pdfUrl = rootUrl + element[1:] + '.pdf'
    outputFilePath = outputDirPath + pdfUrl.split("/")[-1]
    if not os.path.exists(outputFilePath):
    	urllib.request.urlretrieve(pdfUrl, outputFilePath)
    sys.stdout.write("%d/%d have completed!\r" % (i + 2, pdfUrl_sum))
    sys.stdout.flush()
print("\nfinish!")
