from VideoGenerator import VideoGenerator

generator = VideoGenerator("D:\MassProduction", 2, 1)
#Video Files
generator.SelectVideoFiles()
#Pick Image File
generator.SelectImageFile()
#Write Description

#Generate the Video with FFMPEG

#Upload to YouTube

#Clean up files
generator.CleanUpTest()