# ScrapingImages
Scraping Images with Python |
Coded by Hoyeol Kim

### Scraping a Single Image File from a Website
If you want to download a single image file from a website, use the following code from [ImageCrawling_Single.py](https://github.com/elibooklover/ScrapingImages/blob/master/ImageCrawling_Single.py):

```python3
import urllib.request
import os

# Change the URL
url = "https://charlesdickenspage.com/illustrations-web/Nicholas-Nickleby/nicholas-nickleby01.jpg"

# Set the path and filename
outpath = "/Users/hoyeolkim/Downloads/"
outfile = "test.png"

urllib.request.urlretrieve(url, outpath+outfile)
print("complete!")
```

### Scraping Multiple Image Files from a Website
If you want to scarp multiple files from a website, use the following code from [ImageCrawling_Multiple.py](https://github.com/elibooklover/ScrapingImages/blob/master/ImageCrawling_Multiple.py):

```python3
import urllib.request
import os

count = 1
while count < 100:
    print(count)
    
    # Change the path, URL, and fileform
    outpath = "/Users/hoyeolkim/Documents/pix2pix/photos/Dickens/HauntedMan/"
    url = "https://charlesdickenspage.com/illustrations-web/The-Haunted-Man/The-Haunted-Man"
    count1 = str(count) 
    fileform = count1.zfill(2) + ".jpg"
    urllib.request.urlretrieve(url+fileform, outpath+fileform)
    count = count + 1
else:
    print("complete!")
```
