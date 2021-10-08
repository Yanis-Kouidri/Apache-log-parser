#!/usr/bin/python3

#This file will read the lines and parse them into a dictionnary
#that will be returned to the main.

import re

#parse function will take the file in input and process it into dictionnary
#So a dictionnary should be returned. But there is one dictionnary per line.
#A list is made to hold them
#Dictionnary reset at each line

def reg_check(expression):
    
    return type(re.search("^([^ ]+ ){3}\[[^ ]+ [^ ]+\] \"[A-Z]+ /.+ HTTP\/[0-9]\.[0-9]\" ([0-9]+ ){2}\"https?://.+\" \".+\"",expression).group())

def parse(inputFile):
    result=[]
    with open(inputFile, "r") as opened:
        for line in opened:
            #the file is named "opened", in the loop each line is named line
            processedLine={}
            
            if reg_check(line) == None:
                print("Encountered a broken line")
                result.append("Broken")
            else:

                processedLine['remote_ip']=re.search("([0-9]{1,3}\.){3}[0-9]{1,3}",line).group()
                #Dictionnary appending works, now we need to generate the whole thing
            
                processedLine['time']=re.search("[0-9]{2}\/[A-Z][a-z]*\/[0-9]*(:[0-9]{2}){3} [\+\-][0-9]{4}",line).group()
            
                processedLine['request']=re.search("\"[A-Z]{3,} ",line).group()[1:-1]

                processedLine['referrer']=re.search("\"https?:\/(/[^ \/]+)+\/?\"",line).group()[1:-1]
            
                #processedLine[]=re.search(,line).group()
                result.append(processedLine)

    return result
