#!/usr/bin/python3

#What I want my program to do :
#Parsing and treatment of apache logs, with user input for the file.
#Grab lines one by one, deconcatenate them, and write them, then repeat.
#Grab line, deconcatenate, format in json and write entry, then next.
#read will return a dictionnary per line of logs. We have to store it in a list

import read
import to_json

inputName=str(input("File to process : "))

parsed=read.parse(inputName)
#parsed variable is now a list of dictionnaries

outputName=str(input("Name of the output (default will be the input file name .json, extension is added automatically) : "))

if outputName == "":
    outputName=inputName

to_json.convert(parsed, outputName, inputName)
