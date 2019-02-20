#Functions:
from exp import *

#Lib of functions used in Main.py

# Creates the Exceptions:
def list_exception(exps):
    print(len(exps))
    for exp in exps:
        exp.print_sentence()
    

# Creates the Exceptions:
def create_exceptions(lines):
    exceptions = []
    for line in lines:
        if "Exception" in line:
            E = Exp(line)
            exceptions.append(E)
    return exceptions

# Search a sub string in a list of strings#
def search(lines, sub_string):
    total = []
    for line in lines:
        if int(line.find(sub_string)) > -1:
            total.append(line)
    #print(total)
    return total


# Print line by line:
def print_l(lines):
    for line in lines:
        print(line)

def remove_time(line):
    if (not len(line) > 2) or line.find(" ") == -1:
        return line

    spaces_index = list(find_all(line, ' '))
    pos = spaces_index[1]+1
    return line[pos:]

# Write to file:
def write_file(file, lines):
    print(len(lines))
    with open(file, 'a') as out:
        for line in lines:
            out.write(line+'\n')

# Unique values:
def unique_values(total):
    #print(total[1])[spaces_index[0]:]
    #spaces_index = list(find_all(total[0], ' '))
    #pos = spaces_index[1]+1
    new_total = []

    if not len(total) > 1:
        return total

    new_total = [remove_time(element) for element in total]
    return list(set(new_total))


# Find all spaces - Karl Knechel
def find_all(a_str, sub):
    return [i for i in range(len(a_str)) if a_str.startswith(sub, i)]


# Search a string and print the findings
def search_string_file(lines, search_string, unique, flag_print):#(lines: [str], search_string: str, unique: bool=False, flag_print: bool=False) -> object:
# search_string = "Caused by"
    total = search(lines, search_string)
    
    if unique:
        total_unique = unique_values(total)
        if flag_print:
            print_l(total_unique)
        print("Total of Unique " + search_string + " ", str(len(total_unique)))
        return total_unique

    if flag_print:
        print_l(total)
    print("Total of " + search_string +" found:", str(len(total)))

    return total


# Search google with a site(optional) and queries:
def search_website(total, site=None, top=5):
    import webbrowser
    # search web:
    url = 'https://www.google.com.br/search?q='

    if site is not None:
        url = 'https://www.google.com.br/search?q='+ site

    # Open URL in a new tab, if a browser window is already open.
    limit = (top if top < len(total) else len(total))
    print("XXXXXXXXXXX")
    print(limit)
    print(len(total))
    print(total)
    for i in range(0, limit):
        webbrowser.open_new_tab(url + total[i])