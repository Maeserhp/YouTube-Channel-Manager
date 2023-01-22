from datetime import datetime
import os, random, shutil, glob


class FileManager:
     
    def __init__(self, baseDir: str):    
        self.baseDir = baseDir

        self.musicSourceDir = baseDir+"\Music"
        self.imageSourceDir = baseDir+"\Images"
        self.inProgressDir = baseDir+"\VideoInProgress"
        self.musicDB = baseDir+"\MusicDB.csv"

        self.outputFile = os.path.join(self.inProgressDir, "output.mp4")
        self.dateFormat = "%m-%d-%Y %H-%M-%S"

    def ArchiveAllFiles(self):
        self.ArchiveUsedMusicFiles()
        self.ArchiveUsedImageFiles()
        self.ArchiveVideoInfo()

    def ReturnAndDeleteFiles(self):
        self.MoveMusicFiles()
        self.MoveImageFiles()
        self.DeleteTxtFiles()

    def ReturnFiles(self):
        self.MoveMusicFiles()
        self.MoveImageFiles()

    def ArchiveUsedMusicFiles(self):
        title = "Used-" + datetime.now().strftime(self.dateFormat)
        archivePath = os.path.join( self.musicSourceDir, "UsedMusic", title)
        
        #Create a new file in usedMusic directory with the date time
        os.makedirs(archivePath)
        
        #Move the mp3 files into that directory
        self.MoveMusicFiles(archivePath)


    def ArchiveUsedImageFiles(self):
        title = "Used-" + datetime.now().strftime(self.dateFormat)
        archivePath = os.path.join( self.imageSourceDir, "UsedImages", title)
       
       #Create a new file in usedMusic directory with the date time
        os.makedirs(archivePath)
        
        #Move the png files into that directory
        self.MoveImageFiles(archivePath)


    def ArchiveVideoInfo(self):
        title = "VideoInfo-" + datetime.now().strftime(self.dateFormat)
        archivePath = os.path.join( self.baseDir, "Videos", title)
        
        #Create a new file in usedMusic directory with the date time
        os.makedirs(archivePath)
        
        #Move the txt files into that directory
        txtFiles = glob.glob( self.inProgressDir+"\*.txt")
        for file in txtFiles:
            shutil.move(file, archivePath)

        #Move output.mp4
        shutil.move(self.outputFile, archivePath)



    def MoveMusicFiles(self, dir = None):
        if dir == None : dir = self.musicSourceDir

        usedMusicFiles = glob.glob( self.inProgressDir+"\*.mp3")
        for file in usedMusicFiles:
            shutil.move(file, dir)


    def MoveImageFiles(self, dir = None):
        if dir == None : dir = self.imageSourceDir

        newImage = os.path.join(self.inProgressDir, "newImage.png")
        if os.path.exists(newImage):
            os.remove(newImage)

        usedImageFiles = glob.glob( self.inProgressDir+"\*.png")
        for file in usedImageFiles:
            shutil.move(file, dir)


    def DeleteTxtFiles(self):
        txtFiles = glob.glob( self.inProgressDir+"\*.txt")
        for file in txtFiles:
            os.remove(file)

    def DeleteVideoFiles(self):
        videoFiles = glob.glob( self.inProgressDir+"\*.mp4")
        for file in videoFiles:
            os.remove(file)

    
    #TODO: implement this method
    def CleanArchives(self):
        print("I didn't clean the archives. But I'll try to get to it tommorrow")
