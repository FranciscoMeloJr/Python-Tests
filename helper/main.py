#functions:
#search function:
def search(lines, sub_string):
    # search Caused by:
    total = []
    for line in lines:
        if int(line.find(sub_string)) > -1:
            total.append(line)

    return total

#search function:
def print_l(lines):
    #print
    for line in lines:
        print(line)

#write:
def write_file(file, line):
    with open(file, 'a') as out:
        for line in lines:
            out.write(line+'\n')

#imports:
import sys
import argparse

#main
print("Parser - the arguments are: ", str(sys.argv))

#parser:
parser = argparse.ArgumentParser(description="Parser of Log files")

parser.add_argument("-f","--file", help="File to be parsed: default=server.log")
parser.add_argument("-v","--verbose", help="Show all the file content", action="store_true")
parser.add_argument("-c","--cause", help="Show all the causes", action="store_true")
parser.add_argument("-e","--exception", help="Show all exceptions", action="store_true")
parser.add_argument("-x","--xerror", help="Write all ERROR", action="store_true")
parser.add_argument("-s","--search", help="Returns the 10 url's for each exception found", action="store_true")
parser.add_argument("-k","--kcs", help="Perform the search on the KCS", action="store_true")
parser.add_argument("-g","--google", help="Perform the search on the Google", action="store_true")
parser.add_argument("-w","--write", help="Write all Exceptions to file: defult=output.out", action="store_true")

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
    total = search(lines, "ERROR")
    print("Total of 'ERROR' found:", str(len(total)))

if args.cause:
    # search Caused by:
    total = search(lines, "Caused by")
    print("Total of 'Caused by' found:", str(len(total)))

if args.exception:
    # search Caused by:
    total = search(lines, "Exception")
    print("Total of 'Exceptions' found:", str(len(total)))

if args.search:
    #search
    print("search")

if args.kcs:
    import webbrowser
    # search web:
    site = 'site:www.https://access.redhat.com/solutions'
    url = 'https://www.google.com.br/search?q=' + site + '+'

    # Open URL in a new tab, if a browser window is already open.
    for line in total:
        webbrowser.open_new_tab(url + line)

#google search
if args.google:
    import webbrowser
    # search web:
    url = 'https://www.google.com.br/search?q='

    # Open URL in a new tab, if a browser window is already open.
    for line in total:
        webbrowser.open_new_tab(url + line)

#print
if args.verbose:
    print_l(lines)

#write
if args.write:
    write_file("output.out", lines)

#close file:
f.close()
