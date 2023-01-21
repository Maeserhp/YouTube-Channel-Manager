#Check the encoding of the csv file. I don' think this actually works though
#with open('D:\MassProduction\MusicDB.csv') as f:
    #print(f)

#Test enumerate
# links = ['apple', 'banana', 'orange', 'grape']
# for idx, link in enumerate(links):
#     print(f'{link} is in position {idx} in the list')

#Test string litteral
description = "Hello\nWorld"
description = '%'.join(description.splitlines())

print (description)
