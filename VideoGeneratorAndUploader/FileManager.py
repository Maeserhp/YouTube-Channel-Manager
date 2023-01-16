import os, random, shutil, glob


class FileManager:
     
    def __init__(self, baseDir: str):    
        self.baseDir = baseDir

        self.musicSourceDir = baseDir+"\Music"
        self.imageSourceDir = baseDir+"\Images"
        self.inProgressDir = baseDir+"\VideoInProgress"
        self.musicDB = baseDir+"\MusicDB.csv"

    def CleanUpTest(self):
        self.ReturnMusicFiles()
        self.ReturnImageFiles()
        self.DeleteTxtFiles()

    def ReturnMusicFiles(self):
        usedMusicFiles = glob.glob( self.inProgressDir+"\*.mp3")
        for file in usedMusicFiles:
            shutil.move(file, self.musicSourceDir)

    def ReturnImageFiles(self):
        newImage = os.path.join(self.inProgressDir, "newImage.png")
        os.remove(newImage)

        usedImageFiles = glob.glob( self.inProgressDir+"\*.png")
        for file in usedImageFiles:
            shutil.move(file, self.imageSourceDir)

    def DeleteTxtFiles(self):
        txtFiles = glob.glob( self.inProgressDir+"\*.txt")
        for file in txtFiles:
            os.remove(file)
