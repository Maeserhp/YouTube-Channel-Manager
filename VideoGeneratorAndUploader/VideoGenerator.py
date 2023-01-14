import os, random, shutil, glob

class VideoGenerator:

    def __init__(self, baseDir: str, trackNum: int, repeatNum:int):    
        self.baseDir = baseDir
        self.trackNum = trackNum
        self.repeatNum = repeatNum

        self.musicSourceDir = baseDir+"\Music"
        self.imageSourceDir = baseDir+"\Images"
        self.inProgressDir = baseDir+"\VideoInProgress"
        self.musicDB = baseDir+"\MusicDB.csv"

        self.imageExtensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]


    def SelectVideoFiles(self):
        #Using for loop to randomly choose multiple files
        for i in range(self.trackNum):
            #Variable random_file stores the name of the random file chosen
            randomFile = random.choice(glob.glob( self.musicSourceDir+"\*.mp3"))
            #"shutil.move" function moves file from one directory to another
            shutil.move(randomFile,self.inProgressDir)

    def SelectImageFile(self):
        randomFile = random.choice(glob.glob(self.imageSourceDir+"\*.png"))
        #"shutil.move" function moves file from one directory to another
        shutil.move(randomFile,self.inProgressDir)



    def CleanUpTest(self):

        #Move Music Back to the source directory
        usedMusicFiles = glob.glob( self.inProgressDir+"\*.mp3")
        for i in range(len(usedMusicFiles)):
            shutil.move(usedMusicFiles[i], self.musicSourceDir)

        #Move Image back to the source directory
        usedImageFiles = glob.glob( self.inProgressDir+"\*.png")
        for i in range(len(usedImageFiles)):
            shutil.move(usedImageFiles[i], self.imageSourceDir)

        # Archive the text files