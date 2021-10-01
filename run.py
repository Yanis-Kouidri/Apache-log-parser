#!/usr/bin/python3

#What I want my program to do :
#Parsing and treatment of apache logs, with user input for the file.
#Grab lines one by one, deconcatenate them, and write them, then repeat.
#Grab line, deconcatenate, format in json and write entry, then next.
#read will return a dictionnary per line of logs. We have to store it in a list

import read

toRead=str(input("File to process : "))

parsed=read.parse(toRead)
#parsed variable is now a list of dictionnaries

print(parsed)
