#version 1.2 Feb 16 

# imports:
import sys
import argparse
from functions import *
from google_query import *

# parser:
parser = argparse.ArgumentParser(description="Parser of Log files")

parser.add_argument("-f", "--file", help="File to be parsed: default=server.log")
parser.add_argument("-v", "--verbose", help="Show all the file content", action="store_true")
parser.add_argument("-c", "--cause", help="Show all the causes", action="store_true")
parser.add_argument("-e", "--exception", help="Show all exceptions", action="store_true")
parser.add_argument("-x", "--xerror", help="Write all ERROR", action="store_true")
# parser.add_argument("-s","--search", help="Returns the 10 url's for each exception found", action="store_true")
parser.add_argument("-k", "--kcs", help="Perform the search on the KCS", action="store_true")
parser.add_argument("-g", "--google", help="Perform the search on the Google", action="store_true")
parser.add_argument("-u", "--unique", help="Show the unique messages", action="store_true")
parser.add_argument("-w", "--write", help="Write all Exceptions to file: defult=output.out", action="store_true")
parser.add_argument("-a", "--all", help="Show all", action="store_true")
parser.add_argument("-s", "--snraw", help="Show warns", action="store_true")
parser.add_argument("-D", "-d", "--directory", help="Do it for the whole directory", action="store_true")
parser.add_argument("-l", "-L", "--log", help="Redict everything to a log file", action="store_true")


class Simulation:

    def __init__(self, args_dict, file="server.log", top=5):
        self.args_dict = args_dict
        self.file = str(file)
        self.top = top
        self.run()

    def run(self):
        print("XXXXXXXXXXXXXXXX PARSER HELPER XXXXXXXXXXXXXXXXXXXX")
        print("File: "+ self.file)
        # open file:
        args_dict = self.args_dict
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
        if args_dict["xerror"]:
            # search ERROR:
            print("Search Query: ERROR")
            search_string = "ERROR"
            total = search_string_file(lines, search_string, args_dict["unique"], args_dict["verbose"])

        if args_dict["cause"]:
            # search Caused by:
            print("Search Query: Caused by")
            search_string = "Caused by"
            total = search_string_file(lines, search_string, args_dict["unique"], args_dict["verbose"])

        if args_dict["exception"]:
            # search Exception:
            print("Search Query: Exception")
            search_string = "Exception"
            total = search_string_file(lines, search_string, args_dict["unique"], args_dict["verbose"])
            exps = create_exceptions(total)
            
            if len(exps) > 0:
            	exps[0].print_sentence()

        if args_dict["snraw"]:  # if args.warns:
            # search Warns:
            print("Search Query: WARNS")
            search_string = "Warns"
            total = search_string_file(lines, search_string, args_dict["unique"], args_dict["verbose"])

        # if args.search:
        #   search
        #    print("search")

        if args_dict["kcs"]:
            site = 'www.https://access.redhat.com/solutions '
            search_website(total, site, top)

        # google search
        print(args_dict)
        if args_dict["google"]:
            print("=== Google Search ===== ")
            multiple_queries(total, True)

        # print
        if args_dict["verbose"]:
            if len(total) > 0:
                print_l(total)
            else:
                print("There are no exceptions/caused by")

        # write
        if args_dict["write"]:
            if args_dict["unique"]:
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


def helper(gui_flag=False, *,args=None, args_dict=None):
    if args:
        args_dict = vars(args)
    if not gui_flag:
        if not len(sys.argv) > 1:
            print("Please use help")
            return

    if args_dict["log"]:
        redirect()

    if args_dict["directory"]:
        from os import listdir
        from os.path import isfile, join
        import os

        pwd = os.getcwd()

        onlyfiles = [file for file in listdir(pwd) if isfile(join(pwd, file)) if ".log" in file]
        print("Total of: " + str(len(onlyfiles)) + " log files found")
        for file in onlyfiles:
            Simulation(args_dict, file)
    else:
        # main
        print(args_dict)
        print("Arguments::: ", str(sys.argv))
        if args_dict["file"]:
            Simulation(args_dict, args_dict["file"])
        else:
            Simulation(args_dict)

# Call Helper - GUI - dict to args:
def caller_helper(args_dict):
    print("=== Helper Caller - GUI ===")
    helper(True, args_dict=args_dict)

if __name__ == "__main__":
    print("=== Command Line Execution ===")
    args = parser.parse_args()
    opts = vars(args)
    helper(args=args)
