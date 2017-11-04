import os
import urllib.request

img_dir = "./images/"

if not os.path.exists(img_dir):
    os.mkdir(img_dir)
    
image_file = "./NUS-WIDE/NUS-WIDE-urls/NUS-WIDE-urls.txt"

with open(image_file,"r") as file:
    for line in list(file)[1:]:
        line = [item for item in line.split(" ") if item]
        img_url = line[2]
        img_name = img_dir + line[1] + ".jpg"
        try:
            urllib.request.urlretrieve(img_url,img_name)
        except Exception:
            pass