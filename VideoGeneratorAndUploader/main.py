from datetime import datetime
from FileManager import FileManager
from VideoGenerator import VideoGenerator
from VideoUploader import VideoUploader

fileManager = FileManager("D:\MassProduction")
trackNum = 10 #10
repeatNum = 6 #6
generator = VideoGenerator(fileManager, trackNum, repeatNum)
uploader = VideoUploader()
try:
    fileManager.CleanAllArchives()
    generator.SelectVideoFiles()
    generator.SelectImageFile()
    (musicList, description) = generator.GenerateMusicListAndDescription()
    generator.GenerateVideo(musicList)
    title = "Auto Upload Test " + datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    uploader.startUpload(fileManager.outputFile, title, description, 10, "", "private")
except: #Error
    fileManager.ReturnFiles() # move the music and images back
    print ("Video Genenaration failed")
else: #Success
    #fileManager.ReturnAndDeleteFiles()
    fileManager.ArchiveAllFiles() # Archive Music, Images, text, and video
    print ("Video Genenaration Success")



