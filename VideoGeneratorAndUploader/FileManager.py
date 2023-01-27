from datetime import datetime
import os, random, shutil, glob, time


class FileManager:
     
    def __init__(self, baseDir: str):    
        self.baseDir = baseDir

        self.musicSourceDir = os.path.join(baseDir, "Music")
        self.imageSourceDir = os.path.join(baseDir, "Images")
        self.inProgressDir = os.path.join(baseDir, "VideoInProgress")
        self.musicDB = os.path.join(baseDir, "MusicDB.csv")
        self.archivedImages =  os.path.join(self.imageSourceDir, "UsedImages")
        self.archivedMusic =  os.path.join(self.musicSourceDir, "UsedMusic")


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
        archivePath = os.path.join( self.archivedMusic, title)
        
        #Create a new file in usedMusic directory with the date time
        os.makedirs(archivePath)
        
        #Move the mp3 files into that directory
        self.MoveMusicFiles(archivePath)
        self.PrintFileCount(self.musicSourceDir)



    def ArchiveUsedImageFiles(self):
        title = "Used-" + datetime.now().strftime(self.dateFormat)
        archivePath = os.path.join( self.archivedImages, title)
       
       #Create a new file in usedMusic directory with the date time
        os.makedirs(archivePath)
        
        #Move the png files into that directory
        self.MoveImageFiles(archivePath)
        self.PrintFileCount(self.imageSourceDir)



    def ArchiveVideoInfo(self):
        title = "VideoInfo-" + datetime.now().strftime(self.dateFormat)
        archivePath = os.path.join(self.baseDir, "Videos", title)
        
        #Create a new file in usedMusic directory with the date time
        os.makedirs(archivePath)
        
        #Move the txt files into that directory
        txtFiles = glob.glob(self.inProgressDir+"\*.txt")
        for file in txtFiles:
            shutil.move(file, archivePath)

        #Move output.mp4
        if os.path.exists(self.outputFile):
            shutil.move(self.outputFile, archivePath)


    def CleanAllArchives(self):
        self.CleanImageArchive()
        self.CleanMusicArchive()
        self.CleanVideoArchive()

    # If an image has been archived for 6 months we can un-archive it
    def CleanImageArchive(self):
        # 86400 seconds in a day, 30 days in a month, for 6 months
        sixMonthsAgo = time.time() - 86400*30*6
        # print(time.ctime(sixMonthsAgo))
        self.CleanArchiveFile(self.archivedImages, sixMonthsAgo, self.imageSourceDir)
        self.PrintFileCount(self.imageSourceDir)

    # If a song has been archived for 1 month we can un-archive it
    def CleanMusicArchive(self):
        # 86400 seconds in a day, 30 days in a month, for 1 months
        oneMonthsAgo = time.time() - 86400*30
        # print(time.ctime(oneMonthsAgo))
        self.CleanArchiveFile(self.archivedMusic, oneMonthsAgo, self.musicSourceDir)
        self.PrintFileCount(self.musicSourceDir)

    def CleanVideoArchive(self):
         # 86400 seconds in a day, 30 days in a month, for 1 months
        oneMonthsAgo = time.time() - 86400*30
        # print(time.ctime(oneMonthsAgo))
        self.CleanArchiveFile(self.archivedMusic, oneMonthsAgo)

    def CleanArchiveFile(self, archiveFolder, date, newFolder = None):
        usedFolders = os.listdir(archiveFolder)
        for folder in usedFolders:
            usedFolder = os.path.join(archiveFolder, folder)
            # Check the created date of the folder
            folderDate = os.path.getctime(usedFolder)
            if date > folderDate:
                # If there is no new folder to move the items to we can just delete the whole file
                if not newFolder == None:
                    usedFiles = os.listdir(usedFolder)
                    for file in usedFiles:
                        shutil.move(file, newFolder)
                os.remove(usedFolder)


    def MoveMusicFiles(self, dir = None):
        if dir == None : dir = self.musicSourceDir

        usedMusicFiles = glob.glob( self.inProgressDir+"\*.mp3")
        for file in usedMusicFiles:
            if not os.path.exists(os.path.join(dir, os.path.basename(file))):
                shutil.move(file, dir)
            else:
                os.remove(file)

    def MoveImageFiles(self, dir = None):
        if dir == None : dir = self.imageSourceDir

        newImage = os.path.join(self.inProgressDir, "newImage.png")
        if os.path.exists(newImage):
            os.remove(newImage)

        usedImageFiles = glob.glob( self.inProgressDir+"\*.png")
        for file in usedImageFiles:
            if not os.path.exists(os.path.join(dir, os.path.basename(file))):
                shutil.move(file, dir)
            else:
                os.remove(file)


    def DeleteTxtFiles(self):
        txtFiles = glob.glob( self.inProgressDir+"\*.txt")
        for file in txtFiles:
            os.remove(file)

    def DeleteVideoFiles(self):
        videoFiles = glob.glob( self.inProgressDir+"\*.mp4")
        for file in videoFiles:
            os.remove(file)

    def PrintFileCount(self, dir):
        print(f"{dir} contains {len(os.listdir(dir))} files")

