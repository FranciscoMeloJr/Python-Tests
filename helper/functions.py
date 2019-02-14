#Functions:


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


# Write to file:
def write_file(file, line):
    print(len(line))
    with open(file, 'a') as out:
        for line in lines:
            out.write(line+'\n')

# Unique values:
def unique_values(total):
    #print(total[1])[spaces_index[0]:]
    #print(total[1])[spaces_index[1]:]
    spaces_index = list(find_all(total[0], ' '))

    new_total = []
    if len(total) > 1:
        for sentence in total:
            #print(total)
            new_sentence = total[1][spaces_index[1]:]
            new_total.append(new_sentence)

        return list(set(new_total))
    return [total]


# Find all spaces - Karl Knechel
def find_all(a_str, sub):
    return [i for i in range(len(a_str)) if a_str.startswith(sub, i)]


# Search a string and print the findings
def search_string_file(lines, search_string, unique, flag_print):
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