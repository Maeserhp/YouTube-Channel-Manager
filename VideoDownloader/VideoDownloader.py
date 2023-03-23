import glob
from pytube import YouTube
from pathlib import Path
from moviepy.editor import *
import csv
import unicodecsv
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

    def FindMissingFiles(cls):
        #Get a list of song names from the db
        (songsInDB, links) = cls.GetSongsInDB(cls)
        #Get the names of all the downloaded music files. Both in the Music directory and used Music directory
        downloadedSongs = cls.GetAllDownloadedSongs(cls)
        #Compare both lists and see what files are missing
        missingSongsLinks = set()
        for idx, songfromDB in enumerate(songsInDB):
            if not songfromDB in downloadedSongs:
                missingSongsLinks.add(songfromDB)

        duplicateSongs = cls.GetDuplicateDownloadedSongs(cls)
        diff = len(songsInDB) - (len(downloadedSongs) - len(duplicateSongs))
        if not diff == len(missingSongsLinks):
            print("something went wrong")

        print(f"{len(missingSongsLinks)} Files missing")

        for song in missingSongsLinks:
            print(song)


    def FindMissingDBRecords(cls):
        #Get a list of song names from the db
        (songsInDB, links) = cls.GetSongsInDB(cls)
        #Get the names of all the downloaded music files. Both in the Music directory and used Music directory
        downloadedSongs = cls.GetAllDownloadedSongs(cls)
        #Compare both lists and see what is missing in the database
        missingRecords = set()
        for idx, downloadedSong in enumerate(downloadedSongs):
            if not downloadedSong in songsInDB:
                missingRecords.add(downloadedSong)

        print(f"{len(missingRecords)} records are missing in the Database")


    def GetSongsInDB(cls):
        songs = []
        links = []
        with open('D:\MassProduction\MusicDB.csv', 'r', encoding='utf-8') as csv_file:
            # Read through each row of the csv and add the FileName and link to the lists
            csv_reader= csv.reader(csv_file)
            #next(csv_reader)
            for row in csv_reader:
                songs.append(row[1])
                links.append(row[4])
        
        return (songs, links)
        

    def GetAllDownloadedSongs(cls):
        songs = []
        for file in glob.glob(cls.musicDir+"/**/*.mp3", recursive=True):
            songs.append(Path(file).stem)

        print(len(songs))
        return songs

    def GetDuplicateDownloadedSongs(cls):
        songs = set()
        duplicatesDownloaded = []
        for file in glob.glob(cls.musicDir+"/**/*.mp3", recursive=True):
            songName = Path(file).stem
            if songName in songs:
                duplicatesDownloaded.append(songName)
            else: 
                songs.add(songName)
        
        print(str(len(duplicatesDownloaded))+" duplicate songs found")
        return(duplicatesDownloaded)
        




#private methods
    def __ConvertToMP3(cls, mp4File: str, title: str):
        videoClip = VideoFileClip(mp4File)
        audioClip = videoClip.audio
        audioClip.write_audiofile(f'{cls.musicDir}\{title}.mp3')
        audioClip.close()
        videoClip.close()
        os.remove(mp4File)

