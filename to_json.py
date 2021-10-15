#this file is made to convert the dictionnary we made into a magnificent json file...

def convert(elements, name, baseName):
    file = open(name + ".json","w")
    file.write('{\n\n')   #1 tab after
    file.write('\t"logs": "' + baseName + '"\n\n')
    for i in elements:
        