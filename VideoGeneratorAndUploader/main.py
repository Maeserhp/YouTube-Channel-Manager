from FileManager import FileManager
from VideoGenerator import VideoGenerator

fileManager = FileManager("D:\MassProduction")
generator = VideoGenerator(fileManager, 2, 2)
try:
    #Video Files
    generator.SelectVideoFiles()
    #Pick Image File
    generator.SelectImageFile()
    #Write Description
    (musicList, description) = generator.GenerateMusicListAndDescription()
    #Generate the Video with FFMPEG
    generator.GenerateVideo(musicList)
    #generator.GenerateVideoPS()
    #Upload to YouTube
finally:
    #Clean up files
    fileManager.CleanUpTest()