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

    def CleanUpProduction(self):
        self.ArchiveUsedMusicFiles()
        self.ArchiveUsedImageFiles()
        self.ArchiveVideoInfo

    def CleanUpTest(self):
        self.MoveMusicFiles()
        self.MoveImageFiles()
        #self.DeleteTxtFiles()

    def CleanUpFail(self):
        self.MoveMusicFiles()
        self.MoveImageFiles()

    def ArchiveUsedMusicFiles(self):
        title = "Used- " + datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        archivePath = os.path.join( self.musicSourceDir, "UsedMusic", title)
        
        #Create a new file in usedMusic directory with the date time
        os.mkdir(archivePath)
        
        #Move the mp3 files into that directory
        self.MoveMusicFiles(archivePath)


    def ArchiveUsedImageFiles(self):
        title = "Used- " + datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        archivePath = os.path.join( self.musicSourceDir, "UsedImages", title)
       
       #Create a new file in usedMusic directory with the date time
        os.mkdir(archivePath)
        
        #Move the png files into that directory
        self.MoveImageFiles(archivePath)


    def ArchiveVideoInfo(self):
        title = "VideoInfo- " + datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        archivePath = os.path.join( self.baseDir, "Videos", title)
        
        #Create a new file in usedMusic directory with the date time
        os.mkdir(archivePath)
        
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

    def DeleteVidoeFiles(self):
        videoFiles = glob.glob( self.inProgressDir+"\*.mp4")
        for file in videoFiles:
            os.remove(file)
