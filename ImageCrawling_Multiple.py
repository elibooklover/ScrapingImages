import urllib.request
import os

count = 1
while count < 100:
    print(count)
    outpath = "/Users/hoyeolkim/Documents/pix2pix/photos/Dickens/HauntedMan/"
    url = "https://charlesdickenspage.com/illustrations-web/The-Haunted-Man/The-Haunted-Man"
    count1 = str(count) 
    fileform = count1.zfill(2) + ".jpg"
    urllib.request.urlretrieve(url+fileform, outpath+fileform)
    count = count + 1
else:
    print("complete!")