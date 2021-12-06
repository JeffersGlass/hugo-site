import json

def prebuild():
    from googleapiclient.discovery import build

    with open('config.json', 'r', encoding='utf-8') as infile:
        config = json.load(infile)
    api_key = config['yt_api_key']  # Please set your API key

    api_service_name = "youtube"
    api_version = "v3"
    return build(api_service_name, api_version, developerKey=api_key)

def getPlaylistVideos(playlistID, maxVids = 5):
    youtube = prebuild()

    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        maxResults=maxVids,
        playlistId=playlistID
    )

    response = request.execute()
    #print(json.dumps(response, indent=4))
    return (response)

def getUploadsPLFromChannelID(channelID):
    youtube = prebuild()

    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=channelID
    )
    response = request.execute()
    return(response['items'][0]['contentDetails']['relatedPlaylists']['uploads'])

if __name__ == "__main__":
    print(json.dumps(getUploadsPLFromChannelID("UCjgmTMVx2B5_DOB3bCZBq7A"), indent=4))
    print(json.dumps(getPlaylistVideos("UUjgmTMVx2B5_DOB3bCZBq7A"), indent=4))