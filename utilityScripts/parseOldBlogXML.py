import xml.etree.ElementTree as ET
import os
import errno
from bs4 import BeautifulSoup

tree = None

with open("jjggwp-drafts.xml", encoding ='utf-8') as infile:
    tree = ET.parse(infile)

root = tree.getroot()
allItems = root.findall('./channel/item')

postList = list()

#Find all items with a post_type of 'post'
for item in allItems:
    for child in item:
        if child.tag == '{http://wordpress.org/export/1.2/}post_type' and child.text == 'post':
            postList.append(item)

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
        filename = "draft/" + fileTitle + "/index.html"
    else:
        raise TypeError("Posts should all be of type draft")
        filename = "post/" + fileTitle + "/index.html"
    
    #Create the necessary folder structure if it doesn't already exist
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    #Output
    with open(filename, "w+", encoding="utf-8") as outfile:
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