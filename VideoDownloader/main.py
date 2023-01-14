from YouTubeChannelScraper import YouTubeChannelScraper
from VideoDownloader import VideoDownloader

channelId = "UCuw1VDsmOWOldKGLYq6AkVg"

scraper = YouTubeChannelScraper(channelId)
channel = scraper.GetChannel()
playlistId = scraper.GetChannelPlaylistId(channel)
videoIds = scraper.GetVideoIds(playlistId, 10) #last used 1000

print(len(videoIds))

VideoDownloader.DownloadAll(VideoDownloader, videoIds)