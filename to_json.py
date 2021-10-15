#this file is made to convert the dictionnary we made into a magnificent json file...

def convert(elements, name, baseName):
    file = open(name + ".json","w")
    file.write('{\n')   #1 tab after
    file.write('\t"logs": "' + baseName + '"\n\n')
    file.write('\t"lines":\n\t[\n')
    
    for i in elements:
        file.write('\t\t{\n')   #2 tabs before entry
        
        file.write('\t\t\t"remote_ip": "' + i["remote_ip"] + '"\n\n')    #3 tabs for objects
        file.write('\t\t\t"time": "' + i["time"] + '"\n\n')
        file.write('\t\t\t"request": "' + i["request"] + '"\n\n')
        file.write('\t\t\t"response": "' + i["response"] + '"\n\n')
        file.write('\t\t\t"bytes": "' + i["bytes"] + '"\n\n')
        file.write('\t\t\t"referrer": "' + i["referrer"] + '"\n\n')
        file.write('\t\t\t"agent": "' + i["agent"] + '"\n')
        
        file.write('\t\t},\n\n')

    file.write('\n\t]\n}')
    file.close

    print("File " + name + ".json has been written successfully !")
