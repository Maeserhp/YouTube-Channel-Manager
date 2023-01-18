from datetime import datetime
import os
import subprocess

from FileManager import FileManager
from VideoGenerator import VideoGenerator
import upload_video as uploadVideo

fileManager = FileManager("D:\MassProduction")
generator = VideoGenerator(fileManager, 2,2)
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
    subprocess.call([f"python", f"{uploadVideoPath}", f"--file={fileManager.outputFile}", f"--title={title}", f"--description={description}", "--keywords=\"\"", "--category=10", "--privacyStatus=private"], shell = True)

finally:
    #Clean up files
    fileManager.CleanUpTest()