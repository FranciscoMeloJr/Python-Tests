#version 1.2 Feb 14 

# imports:
import sys
import argparse
from functions import *

# parser:
parser = argparse.ArgumentParser(description="Parser of Log files")

parser.add_argument("-f", "--file", help="File to be parsed: default=server.log")
parser.add_argument("-v", "--verbose", help="Show all the file content", action="store_true")
parser.add_argument("-c", "--cause", help="Show all the causes", action="store_true")
parser.add_argument("-e", "--exception", help="Show all exceptions", action="store_true")
parser.add_argument("-x", "--xerror", help="Write all ERROR", action="store_true")
# parser.add_argument("-s","--search", help="Returns the 10 url's for each exception found", action="store_true")
parser.add_argument("-k", "--kcs", help="Perform the search on the KCS", action="store_true")
parser.add_argument("-g", "--google", help="Perform the search on the Google", action="count")
parser.add_argument("-u", "--unique", help="Show the unique messages", action="store_true")
parser.add_argument("-w", "--write", help="Write all Exceptions to file: defult=output.out", action="store_true")
parser.add_argument("-a", "--all", help="Show all", action="store_true")
parser.add_argument("-s", "--snraw", help="Show warns", action="store_true")
parser.add_argument("-D", "-d", "--directory", help="Do it for the whole directory", action="store_true")


class Simulation:

    def __init__(self, args, file="server.log", top=5):
        self.args = args
        self.file = file
        self.top = top
        self.run()

    def run(self):
        print("XXXXXXXXXXXXXXXX PARSER HELPER XXXXXXXXXXXXXXXXXXXX")
        print("File: "+ self.file)
        # open file:
        args = self.args
        top = self.top

        try:
         f = open(self.file, "r")
        except:
            print("File could not be opened")
            return 

        # read lines:
        lines = f.readlines()
        total = []
        if not len(lines) > 0:
            print("::: File empty :::")
            return

        print("Total Lines: " + str(len(lines)))
        if args.xerror:
            # search ERROR:
            print("Search Query: ERROR")
            search_string = "ERROR"
            total = search_string_file(lines, search_string, args.unique,args.verbose)

        if args.cause:
            # search Caused by:
            print("Search Query: Caused by")
            search_string = "Caused by"
            total = search_string_file(lines, search_string, args.unique, args.verbose)

        if args.exception:
            # search Exception:
            print("Search Query: Exception")
            search_string = "Exception"
            total = search_string_file(lines, search_string, args.unique,args.verbose)

        if args.snraw:  # if args.warns:
            # search Warns:
            print("Search Query: WARNS")
            search_string = "Warns"
            total = search_string_file(lines, search_string, args.unique,args.verbose)

        # if args.search:
        #   search
        #    print("search")

        if args.kcs:
            site = 'www.https://access.redhat.com/solutions '
            search_website(total, site, top)

        # google search
        if args.google:
            search_website(total, top)

        # print
        if args.verbose:
            if len(total) > 0:
                print_l(total)
            else:
                print("There are no exceptions/caused by")

            # write
        if args.write:
            if args.unique:
                total_unique = unique_values(total)
                print("Size", len(total_unique))
                write_file("output.out", total_unique)
            else:
                write_file("output.out", total)

                # close file:
        f.close()

        string_return = "No issues Found on file: "+ self.file
        if total:
            string_return = self.file + " Total issues found " + str(len(total))

        return string_return


def helper(args, gui_flag=False):
    if not gui_flag:
        if not len(sys.argv) > 1:
            return

    if args.directory:
        from os import listdir
        from os.path import isfile, join
        import os

        pwd = os.getcwd()

        onlyfiles = [file for file in listdir(pwd) if isfile(join(pwd, file)) if ".log" in file]
        print("Total of: " + str(len(onlyfiles)) + " log files found")
        for file in onlyfiles:
            Simulation(args, file)
    else:
        # main
        print("Arguments::: ", str(sys.argv))
        if args.file:
            Simulation(args, args.file)
        Simulation(args)

# Call Helper - GUI:
def caller_helper(arg_d: dict):
    args = parser.parse_args()
    args.all = False
    args.cause = arg_d["c"]
    args.unique = False
    helper(args, True)

args = parser.parse_args()
helper(args)
