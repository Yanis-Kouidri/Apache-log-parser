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

            try:
                processedLine['remote_ip']=re.search("([0-9]{1,3}\.){3}[0-9]{1,3}",line).group()
                #Dictionnary appending works, now we need to generate the whole thing
            except:
                print("IP is wrong in the line : returning Broken or Empty")
                processedLine['remote_ip']="Broken or Empty"
                count=count+1
            
            try:
                processedLine['time']=re.search("[0-9]{2}\/[A-Z][a-z]*\/[0-9]*(:[0-9]{2}){3} [\+\-][0-9]{4}",line).group()
            except:
                print("Time is wrong in the line : returning Broken or Empty")
                processedLine['time']="Broken or Empty"
                count=count+1

            try:
                processedLine['request']=re.search("\"[A-Z]{3,} ",line).group()[1:-1]
            except:
                print("Request is wrong in the line : returning Broken or Empty")
                processedLine['request']="Broken or Empty"
                count=count+1

            try:
                processedLine['response']=re.search("\" [0-9]{3}",line).group()[2:]
            except:
                print("Response is wrong in the line : returning Broken or Empty")
                processedLine['response']="Broken or Empty"
                count=count+1

            try:
                processedLine['bytes']=re.search("[0-9]+ \"",line).group()[:-2]
            except:
                print("Bytes is wrong in the line : returning Broken or Empty")
                processedLine['bytes']="Broken or Empty"
                count=count+1

            try:
                processedLine['referrer']=re.search("\"https?:\/(/[^ \/]+)+\/?\"",line).group()[1:-1]
            except:
                print("Referrer is wrong in the line : returning Broken or Empty")
                processedLine['referrer']="Broken or Empty"
                count=count+1

            try:
                processedLine['agent']=re.search("\"[A-Z]{1}[a-z]+\/.+\..+( .+)*\"",line).group()[1:-1]
            except:
                print("Agent is wrong in the line : returning Broken or Empty")
                processedLine['agent']="Broken or Empty"
                count=count+1

                #processedLine[]=re.search(,line).group()
            result.append(processedLine)
    
    print(str(count) + " defective or empty elements have been reported")

    return result
