
#imports:
import sys
import argparse
from functions import *

#main
print("Parser - the arguments are: ", str(sys.argv))

#parser:
parser = argparse.ArgumentParser(description="Parser of Log files")

parser.add_argument("-f","--file", help="File to be parsed: default=server.log")
parser.add_argument("-v","--verbose", help="Show all the file content", action="store_true")
parser.add_argument("-c","--cause", help="Show all the causes", action="store_true")
parser.add_argument("-e","--exception", help="Show all exceptions", action="store_true")
parser.add_argument("-x","--xerror", help="Write all ERROR", action="store_true")
#parser.add_argument("-s","--search", help="Returns the 10 url's for each exception found", action="store_true")
parser.add_argument("-k","--kcs", help="Perform the search on the KCS", action="store_true")
parser.add_argument("-g","--google", help="Perform the search on the Google", action="store_true")
parser.add_argument("-u","--unique", help="Show the unique messages", action="store_true")
parser.add_argument("-w","--write", help="Write all Exceptions to file: defult=output.out", action="store_true")
parser.add_argument("-a","--all", help="Show all", action="store_true")
parser.add_argument("-s","--snraw", help="Show warns", action="store_true")
parser.add_argument("-D","-d","--directory", help="Do it for the whole directory", action="store_true")


args = parser.parse_args()

#default file:
file = "server.log"

if args.file:
    # search Caused by:
    file = str(args.file)

#open file:
f = open(file, "r")

#read lines:
lines = f.readlines()

if args.xerror:
    # search Caused by:
    search_string = "ERROR"
    total = search(lines, "ERROR")
    print("Total of 'ERROR' found:", str(len(total)))
    if args.unique: 
        total_unique = unique_values(total)
        print("Total of Unique 'Caused by' found:", str(len(total_unique)))

if args.cause:
    # search Caused by:
    print("Caused by")
    search_string = "Caused by"
    total = search(lines, "Caused by")
    print("Total of 'Caused by' found:", str(len(total)))
    if args.unique: 
        total_unique = unique_values(total)
        print("Total of Unique 'Caused by' found:", str(len(total_unique)))

if args.exception:
    # search Caused by:
    print("Exception")
    search_string = "Exception"
    total = search(lines, "Exception")
    print("Total of 'Exceptions' found:", str(len(total)))
    if args.unique: 
        total_unique = unique_values(total)
        print("Total of Unique 'Exceptions' found:", str(len(total_unique)))

if args.snraw: #if args.warns:
    # search Warns:
    print("Warns")
    search_string = "Warns"
    total = search(lines, search_string)
    print("Total of 'Warns' found:", str(len(total)))
    if args.unique: 
        total_unique = unique_values(total)
        print("Total of Unique 'Warns' found:", str(len(total_unique)))

#if args.search:
#   search
#    print("search")

if args.kcs:
    import webbrowser
    # search web:
    site = 'site:www.https://access.redhat.com/solutions'
    url = 'https://www.google.com.br/search?q=' + site + '+'

    # Open URL in a new tab, if a browser window is already open.
    top = 5
    for i in range(5):
        webbrowser.open_new_tab(url + total[i])

#google search
if args.google:
    import webbrowser
    # search web:
    url = 'https://www.google.com.br/search?q='

    # Open URL in a new tab, if a browser window is already open - limit is 10:
    top = 5
    for i in range(5):
        webbrowser.open_new_tab(url + total[i])

#print
if args.verbose:
    if len(total) > 0:
        print_l(total)
    else:
        print("There are no expceptions/caused by")

#write
if args.write:
    if args.unique: 
        print("Size", len(total_unique))
        write_file("output.out", total_unique)
    else:
        write_file("output.out", total)

#do it for the whole directory:
if args.directory:
    from os import listdir
    from os.path import isfile, join
    
    import os
    pwd = os.getcwd()

    onlyfiles = [file for file in listdir(pwd) if isfile(join(pwd, file)) if ".log" in file]
    for file in onlyfiles:
        print(file)

#close file:
f.close()
