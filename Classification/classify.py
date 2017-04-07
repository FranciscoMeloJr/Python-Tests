#!/usr/bin/python
import sys
'''
Created on Nov 1, 2016

@author: francis with changes of Francisco
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.tools.plotting import bootstrap_plot
import random

import pylab

import matplotlib.pyplot as plt

import math

import pdb

import plotly
import plotly.plotly as py

import os

from printdebug import debug

from execution import Execution
from csv_module import *
from classification_module import *

# # Class used for the tests:
# class Run(object):
#     info = []
#     classification = []
#
#     def __init__(self, init_value):
#         self.info = init_value
#
#     def set_classification(self, data):
#         self.classification = data
#
#     def print_(self):
#         print
#         self.info
#         print
#         self.classification
#
#     def __str__(self):
#         str1 = ''.join(self.info)
#         return str1
#
#     def get_info(self):
#         return self.info
#
#     def get_classification(self):
#         return self.classification


"This function merges everything to put in a dictionary"
def merge(data, result):
    print "Result"
    #sample        group
    #1037.898209   2

    #id     guess      samples  tag
    #847       0   205.235228    0

    #id     group      samples  tag
    #847       0/1  205.235228    0

    list_data = data['samples']
    list_guess = data['guess'].copy()
    list_groups = result['guess']
    list_sample = result['result']
    
    list_tag = data['tag']
    
    #iterating:
    k = 0
    while k < len(list_sample):
        aux = list_sample[k]
        j = 0
        while j < len(list_data):
            if list_data[j] == aux:
                list_guess[j] = list_groups[k]
            j+=1
        k+=1
        
    return ({'samples': list_data, 'tag': list_tag, 'guess': list_guess})


"This function will call the automated classification with variance"
def doClassification_using_variance(mix, print_flag, plot_flag):
    return testClassification(mix, print_flag, plot_flag)

"This function will call the automated classification with ranges"
def doClassification_using_range(mix, print_flag, plot_flag):
    return testClassification_range(mix, print_flag, plot_flag)

"This function will call the automated classification with ranges"
def doClassification_specific_range(mix, groups = 3, print_flag = 0 , plot_flag = 0):
    return testClassification_specific_range(mix, groups, print_flag, plot_flag)

"Creating a normal distribution"
def normal_distribution():
    ok = Gauss(200, 50).gen_samples(100, 0)
    bad = Gauss(500, 50).gen_samples(100, 1)
    
    mix = pd.concat([ok, bad], ignore_index=True)
    
    #np.random.shuffle(mixed)
    mix = mix.reindex(np.random.permutation(mix.index))
    print(mix)
    
    plt.figure()
    plt.subplot(2, 1, 1)
    bins = 50 
    alpha = 0.5
    ok.samples.plot(kind='hist', alpha=alpha)
    bad.samples.plot(kind='hist', alpha=alpha)
    plt.subplot(2, 1, 2)
    mix.samples.plot(kind='hist', bins=bins)
    plt.savefig("mix.png")
    plt.show()
    
    return ok

"Plot"
def plot(x, y, labely, labelx):
    #plt.plot([1,2,3,4])
    
    pylab.plot(x, y, '-b', label='sine')
    plt.ylabel(labely)
    plt.xlabel(labelx)
    plt.show()
    
    return plt


"This function finds the classification"
def find_group(test, number, print_flag):
    "Find group"
    j = 0
    if(print_flag > 0):
        for each in test:
            print each
    
    for each in test:
        i = 0
        for i in range(len(each)):
            if(each[i] == number):
                return j    
        j+=1
    return -1

"This function connects for each run and the values of each metric"
def connect(test, print_flag):
    "Connect"
    totalRun = []
    position = 0
    while position < 50:
        run = []
        for each in test:
            run.append(each[position])
            
        totalRun.append(run)
        position+=1

    if(print_flag > 0):
        print totalRun

    return totalRun

"This function classify each run"
# Data: [[2, 3, 1, 1088], [2, 3, 1, 1088], [2, 3, 1, 1089]
# Result: [[2, 2, 2, 2], [2,3,4,5]]
def classify_each_run(data, result_classification, print_flag):
    print "Classify each run"

    index = 0
    max = 4
    position_in_list = 0
    
    list_aux = []
    list_aux1 = [[1,2,4,5,6],[3,4,5,6]]
    list_aux2 = [[0,2,4,5,6],[3,3,5,8]]
    
    list_aux.append(list_aux1)
    list_aux.append(list_aux2)
    if(print_flag > 0):
        print data
        
    allResults = []
    max = 5
    for each in data:
            temp = [] #[1,1,1,0]
            i = 0
            while i < max:
                    aux = each[i]
                    result = find_group(result_classification[i], aux, 0)
                    temp.append(result)
                    i+=1                  
            allResults.append(temp) #[[1,1,1,0],[1,1,1,0]]
            
    return allResults

"This function analysis the classification of the executions"
def analysis_executions(list_groups, counter):
    print "Analysis"

    total  = 0
    percentage = []
    for eachGroup in list_groups:
        total+= len(eachGroup)

    for eachGroup in list_groups:
        numerator = len(eachGroup)
        percentage.append(numerator/float (total))

    #writes to csv:
    list_each = []
    list_write = []
    gr = 0
    for each in percentage:
        list_each = ["metric" + str(counter), each, gr]
        list_write.append(list_each)
        gr = gr + 1

    #list_write = ["metric" + counter,, "group1"], ["metric123", "50", "group2"]
    csv_write_append("results/egg.csv",list_write , True)

    return percentage
"This function analysis the classification within the runs:"
def analysis(list_runs):
    print "Analysis"
    temp = []
    types = []
    types_list = []
    result = []
    j = 0
    max = 5
    while j < max:
        for each in list_runs:
            info = each.get_classification()
            temp.append(info[j])

        types.append(temp[0])
        
        for i in range(len(temp)):
            if(temp[i] not in types):
                types.append(temp[i])

        result = find_types(types)
        types_list.append(result)
        j+=1

    #[[1, 0], [1, 0, 2], [1, 0, 2], [1, 0, 2], [1, 0, 2]]
    print types_list

    i = 0
    list_info = []
    for each in types_list:
        print each
        for j in range(len(each)):
            calculate_correlation(each[j], list_runs,i)
        i+=1
           
    return 0


"this function calculates the correlation of a specific number, in a index, to the classification"
def calculate_correlation(specific, list_runs, index):
    print 'calculate correlation metric:' + str(index)
    print 'group:' + str(specific)
    
    result = []
    temp = []
    total = 0
    for each in list_runs:
        info = each.get_classification()
        if (info[index] is specific):
            #print info
            total +=1
            result.append(info)

    #Count the repetitions or similarities:
    similarities(index, specific, result)
    
    return result

"this function finds the types of a distribution"
def similarities(index, specific, result):
    print 'relations'
    sim = []
    position = 0
    po_0 = []
    sum_po_0 = []
    po_1 = []
    po_2 = []
    po_3 = []
    po_4 = []
    dict = {}
    for each in result:
        for position in range(len(each)):
            if(position is not index):
                if(position is 0):
                    #if(each[position] not in po_0):
                    po_0.append(each[position])
                        
                if(position is 1):
                    #if(each[position] not in po_1):
                    po_1.append(each[position])
                if(position is 2):
                    #if(each[position] not in po_2):
                    po_2.append(each[position])
                    
                if(position is 3):
                    #if(each[position] not in po_3):
                    po_3.append(each[position])
                        
                if(position is 4):
                    #if(each[position] not in po_4):
                    po_4.append(each[position]) 
        
    sim.append(po_0)
    sim.append(po_1)
    sim.append(po_2)
    sim.append(po_3)
    sim.append(po_4)
    if not sim:
        print("List is empty")
    else:
        print sim

    x = 10
    print "Porcentagem de relacao " + str(x)
    
    
"Find the types of a distribution"
#this function finds the types of a distribution:
def find_types(temp):
    types = []
    types.append(temp[0])
    for i in range(len(temp)):
        if(temp[i] not in types):
            types.append(temp[i])

    return types

"Plotly function"
#this function tests plotly - data = [[0, 3], [1, 3], [2, 14] ]
def test_plot(data, print_flag, plot, i):
    #[[0, 3], [1, 3], [2, 14] ]
    #data = [[0, 3], [1, 3], [2, 14] ]
    
    tempx = []
    tempy = []
    if(print_flag > 0):
        debug(data)
        
    for each in data:
        print each
        tempx.append(each[0])
        tempy.append(each[1])

    plt.title('Classification ' + str(i))
    plt.xlabel('Group number')
    plt.ylabel('Quantity')
    plt.plot(tempx, tempy, 'ro')
    max = 50
    x_lim = 4
    plt.axis([0, x_lim, 0, max])
    if(plot):
        plt.show()
    name = str(i)+".svg"
    plt.savefig(name, transparent = True)

"This function does a histogram"
def do_histogram(data, print_flag):
    #[[0,2,2],[1,1,1],[4,4,4]] -> [0,3] [1,3]
    print "do histogram"
    if(print_flag):
        print data

    initial_number = 1
    j = initial_number
    temp = []
    for each in data:
        count = 0
        for eachm in each:
            count +=1
        aux = []
        aux.append(j)
        aux.append(count)
        temp.append(aux)
        j+=1
        
    return temp


"This function will create the runs (the classe defined above)"
def create_list_Executions_object(list_metrics, flag):
    list_objects = []
    i = 0
    for each in list_metrics:
        x = Execution(i, each)
        list_objects.append(x)
        if(flag):
            x.show()
        i = i + 1


    return list_objects

"This function prints the classification for each execution"
def printClassification(list_executions):
    for each in list_executions:
        print each.get_classification()

"This function will take a specific metric from a list of runs Objects"
def take_index_metrics(list_executions, index, flag):
    print index
    list_metrics_index = []
    for each in list_executions:
        list_metrics_index.append(each.get_index_metrics(index))

    if(flag):
        print list_metrics_index

    return list_metrics_index

"This function will print each run"
def printExecutions(list_runs):
    for each in list_runs:
        each.show()

"This function finds a position of a value in a list of lists"
def find_position(value, list_values):
    i = 0
    for eachList in list_values:
        for each in eachList:
            if (int(each) == value):
                return i
        i = i + 1
    #not found:
    return -1

"This function will take put the classification for each group, and put the result in the position"
def do_classification(list_executions, eachCollumn_result, metric_position, flag):
    print metric_position
    i = 0
    groups = eachCollumn_result
    # for each in groups:
    #     print i
    #     i = i + 1

    for each in list_executions:
        metric_value = int(each.get_index_metrics(metric_position))
        classification = each.get_classification()
        if(flag):
            print metric_value
        result = find_position(metric_value, groups)
        classification[metric_position] = result
        each.set_classification(classification)

"This function will create the header in the csv file"
def createHeader(path, flag):
    csv_write_csv(path, [['metric', 'percentage', 'group']], flag)


"This function write the results in a csv file"
def writeResult(path, list_executions, flag = False):

    for each in list_executions:
        temp = []
        if(flag):
            print each.get_classification()
        temp.append(each.get_classification())
        csv_write_list(path, temp, True)

"This function will create the runs from the csv file Josias"
def createExecutions(path, print_flag):
    temp_data = csv_read_full(path, True)
    if(len(temp_data) > 0):
        list_executions = create_list_Executions_object(temp_data, False)
        print len(list_executions)
    else:
        print "Empty list of executions"

    # getchar()
    raw_input("Press Enter to continue...")

    print temp_data

    #To print the execution
    if(print_flag):
        printExecutions(list_executions)

    #take a metric:

    #Classify each collumn:
    j = 0
    max = 3
    createHeader("results/egg.csv", False)
    while j < max:
        result = []
        eachCollum = take_index_metrics(list_executions, j, False)

        #testClassification(mix, print_flag, plot_flag):
        eachCollumn_result = doClassification_specific_range(eachCollum, 2, 0, 0)
        data = do_histogram(eachCollumn_result, False)
        test_plot(data, 1, j, False)
        result.append(eachCollumn_result)
        if (print_flag):
            print 'result'
            print eachCollumn_result

        #do the classification
        do_classification(list_executions, eachCollumn_result, j, False)
        #show the classification
        if(print_flag):
            printClassification(list_executions)

        #percentage calculation:
        if(print_flag):
            print(analysis_executions(eachCollumn_result, j))

        #getchar()
        raw_input("Press Enter to continue...")
        j = j + 1

    writeResult("results/classification.csv", list_executions)


"Main function"
def main(path = "testsFiles/troubleSample.csv"):
    #testCSV()
    createExecutions(path, False)

# "calling main"
# if __name__ == '__main__':
#     main()


if(len(sys.argv)> 1 ):
    print sys.argv[1]
    main(sys.argv[1])
else:
    main()