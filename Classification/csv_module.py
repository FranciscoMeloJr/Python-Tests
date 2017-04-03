
"Function to read the csv with path"
import os
import csv

"This function reads an specific position in the csv:"
def csv_read(position, path):
    # position = 0
    temp = []
    script_dir = os.path.dirname(__file__)
    path = "testsFiles/troubleSample.csv"
    rel_path = path
    # path = 'src/troubleSample.csv'
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if (len(row) > position):
                temp.append(int(row[position]))

    return temp

"This function reads the whole csv file to create each execution"
def csv_read_full(path, ignore_header = False):
    # position = 0
    temp = []
    script_dir = os.path.dirname(__file__)
    rel_path = path  # = 'src/troubleSample.csv'
    abs_file_path = os.path.join(script_dir, rel_path)
    i = 0
    with open(abs_file_path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            temp.append(row)
            # if (len(row) > position):
            #    temp.append(int(row[position]))

    if (ignore_header):
        temp = temp[1:]
    return temp


"This function writes to a csv file"
def csv_write_csv(path, header, flag):
    if(flag):
        print path
    with open(path, 'wb') as csvfile:
        csv_out = csv.writer(csvfile, header)
        for each in header:
            csv_out.writerow(each)


"This function appends to a csv file"
def csv_write_append(path, content, flag):
    if(flag):
        print path
    with open(path, 'a') as csvfile:
        csv_out = csv.writer(csvfile, content)
        for each in content:
            csv_out.writerow(each)  # Write out each account as a row

"This function appends to a csv file [1,2,3,4]"
def csv_write_list(path, content, flag):
    if (flag):
        print
        path

    with open(path, 'a') as csvfile:
        csv_out = csv.writer(csvfile, content)
        for each in content:
            csv_out.writerow(each)  # Write out each account as a row
