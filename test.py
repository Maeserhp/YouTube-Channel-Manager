from VideoGeneratorAndUploader.FileManager import FileManager


#Check the encoding of the csv file. I don' think this actually works though
#with open('D:\MassProduction\MusicDB.csv') as f:
    #print(f)

#Test enumerate
# links = ['apple', 'banana', 'orange', 'grape']
# for idx, link in enumerate(links):
#     print(f'{link} is in position {idx} in the list')

#Test string litteral
# description = "Hello\nWorld"
# description = '%'.join(description.splitlines())

# print (description)

#Test printing number
# num = 2
# thing = "thing"
# print (f'{thing}-{num}')

#test archive
fileManager = FileManager("D:\MassProduction")
#fileManager.ArchiveVideoInfo()
#fileManager.CleanImageArchive()
#fileManager.ReturnAndDeleteFiles()
fileManager.ArchiveAllFiles()


