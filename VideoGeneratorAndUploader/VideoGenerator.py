#packages
import mutagen
from mutagen.mp3 import MP3

#
import os, random, shutil, glob, datetime, csv

#local
from FileManager import FileManager

class VideoGenerator():

    def __init__(self, fileManager: FileManager, trackNum, repeatNum):    
        self.fileManager = fileManager
        
        self.trackNum = trackNum
        self.repeatNum = repeatNum

    def SelectVideoFiles(self):
        #Using for loop to randomly choose multiple files
        for i in range(self.trackNum):
            #Variable random_file stores the name of the random file chosen
            randomFile = random.choice(glob.glob( self.fileManager.musicSourceDir+"\*.mp3"))
            #"shutil.move" function moves file from one directory to another
            shutil.move(randomFile, self.fileManager.inProgressDir)

    def SelectImageFile(self):
        randomFile = random.choice(glob.glob(self.fileManager.imageSourceDir+"\*.png"))
        #"shutil.move" function moves file from one directory to another
        shutil.move(randomFile, self.fileManager.inProgressDir)

    def GenerateDescription(self):
        filePathCol = 0
        fileNameCol = 1
        youTubeLinkCol = 4
        listenLinkCol = 5

        description = "Thank you for watching this video. I hope you enjoy this collection of lofi music! Please consider liking this video and subscribing to our channel. It would help us out so much and help other people like you find this great music. \n\n#lofi #chill #lofihiphop \n\nTracklist and Credits:\n"
        totalTime = 0

        #Put the csv data into a list
        fileData = []
        pathCol = []
        with open('D:\MassProduction\MusicDB.csv', 'r') as csv_file:
            reader= csv.reader(csv_file)
            next(reader) #this code either skips the headers or skips the fist record
            for row in reader:
                fileData.append(row)
                pathCol.append(row[filePathCol])

        for i in range(self.repeatNum):
            musicFiles = glob.glob( self.fileManager.inProgressDir+"\*.mp3")
            for file in musicFiles:
                if i == 0:
                    print (file)
                    
                    #Create Time stamp
                    time = datetime.time(hour=0, minute=int(totalTime/60), second=int(totalTime%60))
                    timeStamp = time.strftime('%H:%M:%S')

                    #Get the record from the csv file
                    idx = pathCol.index(file)
                    item = fileData[idx]

                    fileName = item[fileNameCol]
                    youTubeLink = item[youTubeLinkCol]
                    listenLink = item[listenLinkCol]
                    description += f"{timeStamp} {fileName}\nProvided by Lofi Girl\nWatch: {youTubeLink}\nListen: {listenLink}\n\n"

                    #Add the time of the current song
                    mp3Length = MP3(file).info.length
                    totalTime += mp3Length

                #escape any apostrophes
                file = file.replace("'","'\''")
                self.writeTextFile("musicList", f"file '{file}'\n")

        #Add final Time stamp
        time = datetime.time(hour=0, minute=int(totalTime/60), second=int(totalTime%60))
        timeStamp = time.strftime('%H:%M:%S')
        description += f"Listen Again! {timeStamp}\n"

        #Add artist Credit 
        #TODO: if there are more than 1 png files then we have a probelm
        image = glob.glob( self.fileManager.inProgressDir+"\*.png")[0]
        fileName  = os.path.basename(image)
        artistInfo = fileName.split("-")
        artistCredit = f"\nArt Provided by {artistInfo[0]} https://{artistInfo[1]}.com/{artistInfo[2]}"
        description += artistCredit

        #write text file
        self.writeTextFile("myDescription", description)
        

    def writeTextFile(self, fileName:str, text:str):
        path = os.path.join(self.fileManager.inProgressDir, f"{fileName}.txt")
        txtFile = open(path, "a+")
        txtFile.write(text)
        txtFile.close()
        
