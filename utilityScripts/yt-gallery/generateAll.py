from ytgallery import *

myChannelID = "UCjgmTMVx2B5_DOB3bCZBq7A"
myUploads = "UUjgmTMVx2B5_DOB3bCZBq7A"

def generateIndexGallery():
    videos = getPlaylistVideos(myUploads, maxVids=5)
    info = list()
    for vData in videos['items']:
        vid = {
            'id': vData['snippet']['resourceId']['videoId'],
            'title': vData['snippet']['title'],
            'thumbnailURL': vData['snippet']['thumbnails']['high']['url']
            }
        info.append(vid)
    info = info[::-1]

    with open("../../data/indexvideos.json", "w+") as outfile:
        json.dump(info, outfile)


def main():
    generateIndexGallery()

if __name__ == "__main__":
    main()