#this file is made to convert the dictionnary we made into a magnificent json file...

import json

def convert(parsed, name):
    with open(name + ".json","w") as file:

        file.write(json.dumps(parsed, indent=4))

    print("File " + name + ".json has been written successfully !")

    #just converts the file to json with pretty text
