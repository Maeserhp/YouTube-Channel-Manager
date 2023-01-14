from googleapiclient.discovery import build
import credentials as credentials
import csv

class YouTubeChannelScraper:

    def __init__(self, channelId):    
        self.channelId = channelId

        api_service_name = "youtube"
        api_version = "v3"

        self.youTube = build(
            api_service_name, api_version, developerKey=credentials.api_key)


    # Public Methods
    def GetChannel(self):
        request = self.youTube.channels().list(
            part = "snippet,contentDetails,statistics",
            id = self.channelId
        )
        response = request.execute()
        channel = response['items'][0]

        channleName = channel['snippet']['title']
        totalVideoCount = channel['statistics']['videoCount']

        print("Getting Videos for Channel: " + channleName)
        print("Total Videos: " + totalVideoCount)

        return channel

    def GetChannelPlaylistId(self, channel):
        playlistId = channel['contentDetails']['relatedPlaylists']['uploads']
        return playlistId


    def GetVideoIds(self, playlistId, limit:int = None):
        video_ids = []
        maxResults = 50 if limit == None or limit > 50  else limit

        request = self.youTube.playlistItems().list(
                part="snippet,contentDetails",
                playlistId = playlistId,
                maxResults = maxResults)
        response = request.execute()

        for item in response['items']:
            self.__AppendVideoId(item, video_ids, limit)

        nextPageToken = response.get('nextPageToken')
        morePages = True

        
        while morePages:
            if nextPageToken is None or len(video_ids) >= limit:
                morePages = False
            else:
                request = self.youTube.playlistItems().list(
                    part="snippet,contentDetails",
                    playlistId = playlistId,
                    maxResults = 50,
                    pageToken = nextPageToken)
                response = request.execute()

                for item in response['items']:
                    self.__AppendVideoId(item, video_ids, limit)

                nextPageToken = response.get('nextPageToken')

        self.__PruneAlreadyDownloaded(video_ids)

        return video_ids

    # Private Methods
    def __AppendVideoId(self, video, list:list, limit:int):    
        videoId = video['contentDetails']['videoId']
        description = video['snippet']['description']
        videoLink = "https://youtu.be/"+videoId

        #Not working
        #videoLength = video['contentDetails']['duration']
        correctVideoType = "- Watch:" in description and "- Download/Stream:" in description
        
        if correctVideoType and len(list) < limit:
            list.append(videoLink)

    def __PruneAlreadyDownloaded(self, list:list):
        print("Count Before Prune: "+ str(len(list)))
        with open('D:\MassProduction\MusicDB.csv', 'r') as csv_file:
            csv_reader= csv.reader(csv_file)

            next(csv_reader)
            for row in csv_reader:
                if row and row[4] in list:
                    list.remove(row[4])

        print("Count After Prune: "+ str(len(list)))
    



# #This is the channel id of Lofi Girl Records. 
# channelId = "UCuw1VDsmOWOldKGLYq6AkVg"

# # Get credentials and create an API client
# youtubeBuild = build(
#     api_service_name, api_version, developerKey=api_key)

# info = GetChannelInfo(youtubeBuild, channelId)
# playlistId = GetChannelPlaylistId(info)
# videoIds = GetVideoIds(youtubeBuild, playlistId)

# print(len(videoIds))