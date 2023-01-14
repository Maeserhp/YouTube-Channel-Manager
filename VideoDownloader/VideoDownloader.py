from pytube import YouTube
from pathlib import Path
from moviepy.editor import *
import csv
import os

class VideoDownloader:
    #def __init__(self): 
    musicDir = "D:\MassProduction\Music"

    def add_to_csv(cls, youtubeObject: YouTube, link: str):
        #TODO: CHECK TO MAKE SURE THERE ISN'T ALREADY A RECORD OF THIS VIDEO IN THE DATABASE
        name = youtubeObject.title
        description = youtubeObject.description
    
        watchIndex = description.find("- Watch:")
        downloadIndex = description.find("- Download/Stream:")
        endIndex = description.find("📥 | Download this music (free)")
    
        youTubeLink = description[watchIndex+9: downloadIndex].strip()
        downloadLink = description[downloadIndex+19: endIndex].strip()

        file_path = f'D:\MassProduction\VideoInProgress\{name}.mp3'
        #file_name = Path(name).stem
        file_name = name
        artistYtrack = file_name.split(" - ")
        artist_name = artistYtrack[0]
        track_title = artistYtrack[1]

        # list of column names 
        field_names = ['FilePath','FileName','ArtistsName','TrackTitle','YouTubeLink','SpotifyLink','AlbumName']
    
        # Dictionary
        dict = {"FilePath": file_path, "FileName":file_name,"ArtistsName":artist_name,"TrackTitle":track_title,"YouTubeLink": link,"SpotifyLink": downloadLink, "AlbumName":""}

        with open('D:\MassProduction\MusicDB.csv', 'a', newline='') as csv_file:
            dict_object = csv.DictWriter(csv_file, fieldnames=field_names) 
            dict_object.writerow(dict)

    def Download(cls, link: str):
        youtubeObject = YouTube(link)
        audio = youtubeObject.streams.get_lowest_resolution()
        try:
            fileOut = audio.download(cls.musicDir, audio.title)
            cls.__ConvertToMP3(cls, fileOut, audio.title)
            cls.add_to_csv(cls, youtubeObject, link)
        #TODO: Exception not returning correctly
        except Exception as e:
            print("There has been an error in downloading your youtube video: " + str(e))
            return(Exception(e))

        
    def DownloadAll(cls, links:list):
        count = len(links)
        for index, link in enumerate(links):
            try:
                cls.Download(cls, link)
                print(f'Download {index + 1} completed of {count}!')
            except Exception as e:
                print(str(e))
                break


#private methods
    def __ConvertToMP3(cls, mp4File: str, title: str):
        videoClip = VideoFileClip(mp4File)
        audioClip = videoClip.audio
        audioClip.write_audiofile(f'{cls.musicDir}\{title}.mp3')
        audioClip.close()
        videoClip.close()
        os.remove(mp4File)

