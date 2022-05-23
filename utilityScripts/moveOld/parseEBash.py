import xml.etree.ElementTree as ET
import os
import errno
from bs4 import BeautifulSoup
import re
import shutil

tree = None

with open("wordpresspages.xml", encoding ='utf-8') as infile:
    tree = ET.parse(infile)

root = tree.getroot()
allItems = root.findall('./channel/item')

postList = list()

#Find all items with a post_type of 'post'

ebash_pages = []

for item in allItems:
    title = item.find('title')
    if title.text.startswith("Electronics Bash -") and not "Template" in title.text: ebash_pages.append(item)

for page in ebash_pages:
    title = page.find('./title').text
    old_link = page.find('link').text.removeprefix("https://jeff.glass")

    folderName = "eb" + re.search(r"(\d+)", title).group(1)
    fileTitle = "index.html"

    print(f"Processing page {title= } into folder {folderName= }")

    full_path = "../../content/project/electronics-bash/ebash-pages/" + folderName + "/" 
    full_file_path = full_path + fileTitle

    postDate = page.find('{http://wordpress.org/export/1.2/}post_date_gmt').text.replace(" ", "T") + "-05:00"
    content = page.find('{http://purl.org/rss/1.0/modules/content/}encoded').text

    soup = BeautifulSoup(content, 'html.parser')

    print("\tProcessing <p> tags")
    for p in soup.find_all('p'):
        if '[/expand]' in p.contents or '[expand title="Show Code"]' in p.contents: #remove wordpress widgets
            p.extract()
            continue

        if len(p.contents) and 'gist.github' in p.contents[0]:
            link = soup.new_tag('a')
            link['href']=p.contents
            link.string = "Click here to view code on Github"
            p.insert_after(link)
            p.extract()
            continue
        try:
            p['class'].append('post-paragrpah')
        except KeyError as k:
            p['class'] = ['post-paragraph']

    print("\tProcessing <ul> and <h_> tags")
    for ul in soup.find_all('ul'):
        try:
            ul['class'].append('post-ul')
        except KeyError as k:
            ul['class'] = ['post-ul']

    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4']):
        try:
            tag['class'].append(f"post-{tag.name}")
        except KeyError as k:
            tag['class'] = [f"post-{tag.name}"]
    print("\tProcessing <img> tags")

    images_to_copy = []
    
    for img in soup.find_all('img'):
        images_to_copy.append(img['src'])
        new_source = img['src'].split("/")[-1]
        img['src'] = new_source
        try:
            img['class'].append('post-img')
        except KeyError as k:
            img['class'] = ['post-img']

    print("Making folder if necessary")
    #Create the necessary folder structure if it doesn't already exist
    if not os.path.exists(os.path.dirname(full_file_path)):
        try:
            os.makedirs(os.path.dirname(full_file_path))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    print("\tCopying Images")
    for img_src in images_to_copy:
        if 'jeff.glass' in img_src:
            local_path = re.search(r"uploads.+", img_src).group(0)
            image_name = img_src.split("/")[-1]
            dest_path = full_path + image_name
            shutil.copyfile(local_path, dest_path)    

    content = str(soup).replace("\n\n", "\n")    

    #Output
    print("Writing output")
    with open(full_file_path, "w+", encoding="utf-8") as outfile:
        outfile.write("---\n")
        outfile.write("title: \"" + title + "\"\n")
        outfile.write("date: " + postDate + "\n")
        outfile.write("draft: false\n")
        outfile.write("aliases:\n")
        outfile.write("  - " + old_link + "\n")
        outfile.write("---\n")
        if content != None: outfile.write(content)

    print("")

exit()

#For each post, parse the relevent data and output it to a file
for post in postList:
    title = post.find('./title').text
    fileTitle = title.replace(" ", "-").replace(":", "")
    postDate = post.find('{http://wordpress.org/export/1.2/}post_date_gmt').text.replace(" ", "T") + "-05:00"
    if postDate[:4] == '0000': postDate = post.find('{http://wordpress.org/export/1.2/}post_modified_gmt').text.replace(" ", "T") + "-05:00"
    content = post.find('{http://purl.org/rss/1.0/modules/content/}encoded').text
    isDraft = post.find('{http://wordpress.org/export/1.2/}status').text == 'draft'
    tagElements = post.findall("category[@domain='post_tag']")
    tags = [t.attrib['nicename'] for t in tagElements]

    #Preprocess Content
    if content == None:
        print(f"Content from post {post} is None, skipping this file")
        continue
    else:
        content = content.replace("\n\n", "\n")
        newContent = ""
        for line in content.split("\n"):
            if "wp:" in line:
                line = ""
            elif line.strip()[0:3] not in ["<im", "<p>", "<ul", "<li", "<h1", "<h2", "<h3", "<h4", "<fi"]:
                line = "<p>" + line + "</p>\n"
            else: line = line + "\n"
            newContent += line
        content = newContent

    #Add tags to some elements using beautifulSoup
    soup = BeautifulSoup(content, 'html.parser')

    for p in soup.find_all('p'):
        try:
            p['class'].append('post-paragrpah')
        except KeyError as k:
            p['class'] = ['post-paragraph']

    for ul in soup.find_all('ul'):
        try:
            ul['class'].append('post-ul')
        except KeyError as k:
            ul['class'] = ['post-ul']

    for img in soup.find_all('img'):
        try:
            img['class'].append('post-img')
        except KeyError as k:
            img['class'] = ['post-img']
        print(img)

    content = str(soup)
    
    #Use to see all the child elements of a post, to find what the various tags are named
    #for child in post:
    #   print(child.tag)

    #Split drafts and published posts by folder
    if isDraft:
        full_path = "draft/" + fileTitle + "/index.html"
    else:
        raise TypeError("Posts should all be of type draft")
        full_path = "post/" + fileTitle + "/index.html"
    
    #Create the necessary folder structure if it doesn't already exist
    if not os.path.exists(os.path.dirname(full_path)):
        try:
            os.makedirs(os.path.dirname(full_path))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    #Output
    with open(full_path, "w+", encoding="utf-8") as outfile:
        outfile.write("---\n")
        outfile.write("title: \"" + title + "\"\n")
        outfile.write("date: " + postDate + "\n")
        outfile.write("draft: true\n")
        if len(tags) > 0:
            outfile.write("tags:\n")
            for t in tags:
                outfile.write("- " + t + "\n")
        outfile.write("---\n")
        if content != None: outfile.write(content)