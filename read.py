#!/usr/bin/python3

#This file will read the lines and parse them into a dictionnary
#that will be returned to the main.

import re

#parse function will take the file in input and process it into dictionnary
#So a dictionnary should be returned. But there is one dictionnary per line.
#A list is made to hold them
#Dictionnary reset at each line
    
#re.search("^([^ ]+ ){3}\[[^ ]+ [^ ]+\] \"[A-Z]+ /.+ HTTP\/[0-9]\.[0-9]\" ([0-9]+ ){2}\"https?://.+\" \".+\"",expression).group()
#this regex was created to test the fitting of whole linesm ended up unused

def parse(inputFile):
    count=0
    result=[]
    with open(inputFile, "r") as opened:
        for line in opened:
            #the file is named "opened", in the loop each line is named line
            processedLine={}

            cutLine=re.search("(([0-9]*\.){3}[0-9]*).*\[(.*)\].*\"([A-Z]+) .+\" ([0-9]{3}) (.*) \"(.+)\" \"(.+)\"?",line)

            try:
                processedLine['remote_ip']=cutLine.group(1)
                #Dictionnary appending works, now we need to generate the whole thing
            
                processedLine['time']=cutLine.group(3)

                processedLine['request']=cutLine.group(4)

                processedLine['response']=cutLine.group(5)

                processedLine['bytes']=cutLine.group(6)

                processedLine['referrer']=cutLine.group(7)

                processedLine['agent']=cutLine.group(8)

                result.append(processedLine)
            except:
                result.append("Broken")
                count=count+1

                #processedLine[]=re.search(,line).group()
    
    print(str(count) + " defective lines have been reported")

    return result
