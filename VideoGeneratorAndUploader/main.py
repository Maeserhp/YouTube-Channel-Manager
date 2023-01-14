from FileManager import FileManager
from VideoGenerator import VideoGenerator

fileManager = FileManager("D:\MassProduction")
generator = VideoGenerator(fileManager, 2, 2)
#Video Files
generator.SelectVideoFiles()
#Pick Image File
generator.SelectImageFile()
#Write Description
generator.GenerateDescription()
#Generate the Video with FFMPEG

#Upload to YouTube

#Clean up files
fileManager.CleanUpTest()