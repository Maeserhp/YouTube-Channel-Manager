from datetime import datetime
import os
import subprocess

import re
import codecs

from FileManager import FileManager
from VideoGenerator import VideoGenerator
from VideoUploader import VideoUploader

fileManager = FileManager("D:\MassProduction")
trackNum = 10 #10
repeatNum = 6 #6
generator = VideoGenerator(fileManager, trackNum, repeatNum)
uploader = VideoUploader()
try:
    #Video Files
    generator.SelectVideoFiles()
    #Pick Image File
    generator.SelectImageFile()
    #Write Description      
    (musicList, description) = generator.GenerateMusicListAndDescription()
    #Generate the Video with MoviePy
    generator.GenerateVideo(musicList)
    #Upload to YouTube
    uploadVideoPath = os.path.join(".","VideoGeneratorAndUploader", "upload_video.py")
    #description = "test description"
    title = "Auto Upload Test " + datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    # python upload_video.py --file=$inProgressDir\output.mp4 --title=$title --description=$description --keywords="" --category="10" --privacyStatus="private"
    #subprocess.run([f"python", f"{uploadVideoPath}", f"--file={fileManager.outputFile}", f"--title={title}", f"--description={description}", "--keywords=\"\"", "--category=10", "--privacyStatus = unlisted"], check = True, shell = True)
    uploader.startUpload(fileManager.outputFile, title, description, 10, "", "private")
except:
    # If it fails then move the music and images back but keep the txt files
    fileManager.CleanUpFail()
else:
    #fileManager.CleanUpTest()
    fileManager.CleanUpProduction()


