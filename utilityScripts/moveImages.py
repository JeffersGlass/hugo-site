from pathlib import Path
from bs4 import BeautifulSoup
import re
from shutil import copy2

uploadsFolder = './uploads'
postsFolder = '../content/post'

#Get list of all html files in posts
pathlist = Path(postsFolder).glob('**/*.html')


for htmlPath in pathlist:
    #Get contents of file
    path_in_str = str(htmlPath)
    content = None
    with open(path_in_str, "r", encoding='utf-8') as infile:
        content = infile.read()

    soup = BeautifulSoup(content, 'html.parser')
    images = soup.find_all('img')
    print(f"{path_in_str} has {len(images)} img tags:")

    #For each image, pull off just the source path relative to the uploads folder
    for img in images:
        #print(f"\t{img['src']}")
        imgMatch = re.search('jeff.glass\/wp-content\/uploads\/(.+)', str(img['src']))
        if imgMatch != None:
            imgPath = imgMatch.group(1)
            fullImgPath = uploadsFolder + '/' + str(imgPath)
            imgDestination = str(htmlPath.parent)

            #copy2(fullImgPath, imgDestination)
            print(f"\tCopied {fullImgPath} to {imgDestination}", end = ", ")

            imgName = imgPath.split('/')[-1]

            img['src'] = imgName
            print(f"new image is called {imgName}")
        else: imgPath = "EXTERNAL CONTENT, SKIPPING"

