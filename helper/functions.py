#Functions:

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
    print(len(line))
    with open(file, 'a') as out:
        for line in lines:
            out.write(line+'\n')

#unique values:
def unique_values(total):
    #print(total[1])[spaces_index[0]:]
    #print(total[1])[spaces_index[1]:]
    spaces_index = list(find_all(total[0], ' '))

    new_total = []
    if len(total) > 1:
        for sentence in total:
            new_sentence = total[1][spaces_index[1]:]
            new_total.append(new_sentence)

        return set(new_total)
    return total

#Find all spaces:
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)