#!/usr/bin/python3

#This file will read the lines and parse them into a dictionnary
#that will be returned to the main.

import re

#parse function will take the file in input and process it into dictionnary
#So a dictionnary should be returned. But there is one dictionnary per line.
#A list is made to hold them
#Dictionnary reset at each line
    
#re.search("^([^ ]+ ){3}\[[^ ]+ [^ ]+\] \"[A-Z]+ /.+ HTTP\/[0-9]\.[0-9]\" ([0-9]+ ){2}\"https?://.+\" \".+\"",expression).group()
#this regex was created to test the fitting of whole lines and ended up unused

def parse(inputFile):
    count=0
    ipErr=0
    timeErr=0
    reqErr=0
    respErr=0
    bytErr=0
    refErr=0
    agErr=0

    result=[]
    with open(inputFile, "r") as opened:
        for line in opened:
            #the file is named "opened", in the loop each line is named line
            processedLine={}

            try:
                processedLine['remote_ip']=re.search("([0-9]{1,3}\.){3}[0-9]{1,3}",line).group()
                #Dictionnary appending works, now we need to generate the whole thing
            except:
                processedLine['remote_ip']="Broken or Empty"
                count=count+1
                ipErr=ipErr+1
            
            try:
                processedLine['time']=re.search("[0-9]{2}\/[A-Z][a-z]*\/[0-9]*(:[0-9]{2}){3} [\+\-][0-9]{4}",line).group()
            except:
                processedLine['time']="Broken or Empty"
                count=count+1
                timeErr=timeErr+1

            try:
                processedLine['request']=re.search("\"[A-Z]{3,} ",line).group()[1:-1]
            except:
                processedLine['request']="Broken or Empty"
                count=count+1
                reqErr=reqErr+1

            try:
                processedLine['response']=re.search("\" [0-9]{3}",line).group()[2:]
            except:
                processedLine['response']="Broken or Empty"
                count=count+1
                respErr=respErr+1

            try:
                processedLine['bytes']=re.search("[0-9]+ \"",line).group()[:-2]
            except:
                processedLine['bytes']="Broken or Empty"
                count=count+1
                bytErr=bytErr+1

            try:
                processedLine['referrer']=re.search("\"https?:\/(/[^ \/]+)+\/?\"",line).group()[1:-1]
            except:
                processedLine['referrer']="Broken or Empty"
                count=count+1
                refErr=refErr+1

            try:
                processedLine['agent']=re.search("\"[A-Z]{1}([a-z]|[A-Z]| )+([a-z]|[A-Z])+.([0-9]+(\.| ))+.*\"",line).group()[1:-1]
            except:
                processedLine['agent']="Broken or Empty"
                count=count+1
                agErr=agErr+1

                print(line)

                #processedLine[]=re.search(,line).group()
            result.append(processedLine)
    
    print(str(count) + " defective or empty elements have been reported :")
    print(str(ipErr) + " IP adresses fields")
    print(str(timeErr) + " time fields")
    print(str(reqErr) + " request type fields")
    print(str(respErr) + " response code fields")
    print(str(bytErr) + " bytes quantity fields")
    print(str(refErr) + " referrer address fields")
    print(str(agErr) + " agent fields")

    return result
