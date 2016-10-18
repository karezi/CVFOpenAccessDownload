# Only python3 support
import urllib.request
import re
import os

rootUrl = "http://www.cv-foundation.org/openaccess/"
pageUrl = rootUrl + "CVPR2016.py"
html = bytes.decode(urllib.request.urlopen(pageUrl).read())
pdfUrls = re.findall(r'<a href=(.*?).pdf">pdf</a>', html)
for item in pdfUrls:
    pdfUrl = rootUrl + item[1:] + '.pdf'
    print(pdfUrl)
    os.mkdir("./CVPR2016/")
    urllib.request.urlretrieve(pdfUrl, "./CVPR2016/" + item.split("/")[-1])
