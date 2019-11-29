import urllib.request
import os

url = "https://charlesdickenspage.com/illustrations-web/Nicholas-Nickleby/nicholas-nickleby01.jpg"

outpath = "/Users/hoyeolkim/Downloads/"
outfile = "test.png"

urllib.request.urlretrieve(url, outpath+outfile)
print("complete!")
