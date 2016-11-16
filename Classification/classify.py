#!/usr/bin/python3
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

class Gauss(object):
    def __init__(self, mean=0, stddev=1):
        self.mean = mean
        self.stddev = stddev
        
    def gen_samples(self, n, tag=0):
        samples = self.stddev * np.random.randn(n) + self.mean;
        guess = tag
        return pd.DataFrame({'tag': tag, 'samples': samples, 'guess': guess})

class Classification(object):
    """ Constructor for the Classification class: """
    def __init__(self):
        print 'Constructor'

    """ This function calculates the difference of a number in a list:"""
    def calculate_difference(self, data, flag_print, kind):
        #print 'calculate difference'
        result = []
        original = data
        ordered = data.sort()

        i = 1
        #it is a list:
        if(kind > 0):
            list_data = data['samples']
        else:
            list_data = data
        list_difference = []

        #calculate the difference:
        while i < len(list_data):
            #print list_data[i]
            list_difference.append(int(list_data[i]) - int(list_data[i-1]))
            i+=1

        if(flag_print > 0): 
            print len(list_difference)
            
        i = 0
        total_difference = 0
        while i < len(list_difference):
            total_difference += list_difference[i]
            i+=1
                
        #mean:
        total_difference /= len(list_difference)

        return total_difference
    
    """ Variation classification: algorithm using tolerance"""
    def variation_classifier(self, data, tolerance, print_flag, kind):
        
        #mean distance:
        mean_difference = self.calculate_difference(data, 0, kind)
        if(kind > 0):
            list_data = data['samples']
            list_sorted = list_data.copy()
            list_sorted.sort()
            xis = sorted(list_sorted)
            xis = xis.sort()
        else:
            list_data = data
            list_sorted = list_data
            list_sorted.sort()
            xis = data
            
        i = 1
        if(print_flag > 0):
            print xis
        previous = int(xis[0])
        mini_groups = []
        result = []
        if(print_flag > 0):
            print 'Variation classification tolerance'
            print self.valid_numbers(xis)
            
        #tolerance = 0.5
        while i < len(xis):
            temp = float(xis[i])
            if(print_flag > 0):
                print "Value and group"
                print temp
                print len(result)
            #if(temp > previous +(previous * tolerance)):
            comp = float(previous) +(float(previous) / tolerance)
            if(temp > comp):
                result.append(mini_groups)
                mini_groups = []
            mini_groups.append(temp)
            previous = float(temp)
            i+=1
        result.append(mini_groups)
        
        if(print_flag>0):
            print 'Number of groups:'
            print len(result)
            print result

        return result

    """ Function to calcualte the SSE, used for the Elbow method: """    
    def calculate_SSE(self, list_groups, n_groups, flag_print):
        #list_groups[[1,2,3],[4,5,6]]
        centroids = []
        i = 0
        while i < len(list_groups):
            temp = list_groups[i]
            if(len(temp) > 0):
                j = 0
                aux = 0
                while j < len(temp):
                    aux += temp[j]
                    j+=1
                centroids.append(aux/j)
            else:
                centroids.append(0)
            i+=1
        if(flag_print > 0):
            print len(centroids)
            print "Centroid size", centroids
            print "Groups qtd", len(list_groups)
        #SSE Calculation:
        SSE = 0
        i = 0
        k = 0
        while i < len(list_groups):
            x = list_groups[i]
            if(len(x) > 0):
                if(flag_print > 0):
                    print x
                j = 0
                while j < len(x):
                     eachDistance = (x[j] - centroids[i]) * (x[j] - centroids[i])
                     SSE += eachDistance
                     j+=1
            i+=1

        return SSE

    """ Heuristic to evaluate the method """
    def best_k(self, dic):
        list_groups = []
        group1 = []
        list_groups.append(group1)

        #{'n_groups': total_groups, 'sse': total_sse, 'tolerance': total_tolerance})
        n_groups = dic['n_groups']
        tolerance = dic['tolerance']
        calculated_SSE = dic['sse']
        maxp1 = 0        
        minp1 = 0

        i = 1
        gap = 0
        while i < len(calculated_SSE):
            current = calculated_SSE[i -1] - calculated_SSE[i]
            if(current > gap):
                gap = current
                maxp1 = i
            i+=1

        gap = 0
        i = 1
        while i < len(calculated_SSE):
            current = calculated_SSE[i -1] - calculated_SSE[i]
            if(current < gap):
                gap = current
                minp1 = i
            i+=1

        #return minp1
        #return {'b_n_groups': n_groups[maxp1],'b_tolerance': tolerance[maxp1], 'b_sse': calculated_SSE[maxp1]}
        return maxp1
            
        
    """ This is the KDE method classification: """    
    def KDE(self, data):
        print 'KDE'
        while i < len(tag):
            print tag[i]
            i += 1
            
    """ This is the opt_kmeans, which takes the k_means and apply: """
    def Opk_means(self, data):
        elbow = []
        elbow.append(k_means(data, k))

    def k_means(self, data, k):
        print k

    def print_groups(self, data):
        i = 0
        groups = []
        numbers = []
        while i < len(data):
            j = 0
            temp = data[i]
            while j < len(temp):
                print '{0:2f} {1:3d}'.format(temp[j], i+1)
                groups.append(i+1)
                numbers.append(temp[j])
                j+=1
            i+=1
        return {'result': numbers, 'guess':groups}
    
    #validating the sort:
    def valid_numbers(self, data):
        i = 1
        while i < len(data):
            if(data[i - 1] > data[i]):
                return False
            i+=1
        return True
    def kmeans(self, n_groups, n_items, numbers):
        dataItemsD = []
        czD = []
        oldCzD = []
        rowD = []
        groupsD = []

        k1 = n_groups
        noOfItems1 = n_items

        aux = []
        i = 0
        pdb.set_trace()
        while i < k1:
            pdb.set_trace()
            groupsD.append(aux);
            i+=1
        pdb.set_trace()
        dataItemsD = numbers
        i = 0
        while i < len(dataItemsD):
            if (i < k1):
                czD.append(dataItemsD[i])
            i+=1
        ite = 1
        pdb.set_trace()
        while True:
            for aItem in dataItemsD:
                pdb.set_trace()
                for c in czD:
                    rowD.append(abs(c - aItem))
                pdb.set_trace()
                groupsD = self.add(groupsD, rowD.index(min(rowD)), aItem)
                rowD = []
            i = 0
            pdb.set_trace()
            while i < k1:
                if(ite == i):
                    oldCzD.append(czD[i])
                else:
                    oldCzD.insert(i,czD[i])
                if((len(groupsD[i]) > 0)):
                     czD.insert(i, self.averageD(groupsD[i]));
                i+=1
            if(self.equals(czD,oldCzD)== False):
                j = 0
                while j < len(groupsD):
                    groupsD[j] = []
                    j+=1
                i+=1
            ite+=1
            if(self.equals(czD,oldCzD) == False):
                break
        
        return groupsD;
    
    #calculate the average:
    def averageD(self, list_n):
        sum = 0.0;
        i = 0
        while i < len(list_n):
            sum += list_n[i]
            i+=1
        return (sum/len(list_n))

    #equals
    def equals(self, list_x, list_y):
        if (cmp(list_x, list_y) == 0):
           return True
        return False
    
    #add:
    def add(self, list_a, index, aItem):
        i = 0

        while i <= index:
            aux = []
            aux.append('')
            list_a.append(aux)
            i+=1
            
        aux = aItem
        list_a[index] = aux
            
        return list_a
    
#Class used for the tests:
class Run(object):
    info = []
    classification = []
    
    def __init__(self, init_value, init_classification):
        self.info = init_value
        self.classification = init_classification
    
def test():
    #simulation()
    ok = Gauss(200, 50).gen_samples(1000, 0)
    classificator = Classification()
    i = 0

    table = []
    total_groups = []
    total_sse = []
    total_tolerance = []
    print_value = 0
    while i < 3.0:
        if(print_value > 0):
            print "Classification"
        result_groups =  classificator.variation_classifier(ok, i, print_value)
        #print result_groups
        result_sse = classificator.calculate_SSE(result_groups, len(result_groups), print_value)
        print result_sse
        i+=0.1
        hash_tolerance_SSE = []
        hash_tolerance_SSE.append(i)
        hash_tolerance_SSE.append(len(result_groups))
        hash_tolerance_SSE.append(result_sse)

        total_groups.append(len(result_groups))
        total_sse.append(result_sse)
        total_tolerance.append(i)
        
        table.append(hash_tolerance_SSE)
    print table
    
    print classificator.best_k({'n_groups': total_groups, 'sse': total_sse, 'tolerance': total_tolerance})
    
    fig = plt.figure()
    plot(total_tolerance,total_sse, "SSE", "Tolerance")
    plot(total_tolerance,total_groups, "N Groups", "Tolerance")

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
    
def test3():
    print "Test 3"
    print_value = 0

    ok = Gauss(200, 50).gen_samples(1000, 0)
    bad = Gauss(500, 50).gen_samples(100, 1)
    mix = pd.concat([ok, bad], ignore_index=True)
    
    classificator = Classification()
    i = 0.0

    table = []
    total_groups = []
    total_sse = []
    total_tolerance = []
    
    while i < 20:
        if(print_value > 0):
            print "Classification"
        result_groups =  classificator.variation_classifier(mix, i, print_value, 1)
        #print result_groups
        result_sse = classificator.calculate_SSE(result_groups, len(result_groups), print_value)
        #print result_sse
        i+= 1
        hash_tolerance_SSE = []
        hash_tolerance_SSE.append(i)
        hash_tolerance_SSE.append(len(result_groups))
        hash_tolerance_SSE.append(result_sse)

        total_groups.append(len(result_groups))
        total_sse.append(result_sse)
        total_tolerance.append(i)
        
        table.append(hash_tolerance_SSE)
    print table
    
    best_k = classificator.best_k({'n_groups': total_groups, 'sse': total_sse, 'tolerance': total_tolerance})
    print table[best_k]

    print "best tolerance:"
    print round(table[best_k][0],4)
    print "best k:"
    print round(table[best_k][1],4)
    
    result_groups =  classificator.variation_classifier(mix, round(table[best_k][0],4), 0, 1)
    result_splited = classificator.print_groups(result_groups)

    #merge:
    #print merge(mix, result_splited)
    
    fig = plt.figure()
    plot(total_tolerance,total_sse, "SSE", "Tolerance")
    plot(total_tolerance,total_groups, "N Groups", "Tolerance")

    return result_groups

def testClassification(mix, print_value):
    print "Test Classification"
    #mix = pd.concat([ok, bad], ignore_index=True)
    
    classificator = Classification()
    i = 0.1

    table = []
    total_groups = []
    total_sse = []
    total_tolerance = []
    
    while i < 20:
        if(print_value > 0):
            print "Classification"
            print mix
        result_groups =  classificator.variation_classifier(mix, i, print_value, 0)
        #print result_groups
        result_sse = classificator.calculate_SSE(result_groups, len(result_groups), print_value)
        #print result_sse
        i+= 1
        hash_tolerance_SSE = []
        hash_tolerance_SSE.append(i)
        hash_tolerance_SSE.append(len(result_groups))
        hash_tolerance_SSE.append(result_sse)

        total_groups.append(len(result_groups))
        total_sse.append(result_sse)
        total_tolerance.append(i)
        
        table.append(hash_tolerance_SSE)
    print table
    
    best_k = classificator.best_k({'n_groups': total_groups, 'sse': total_sse, 'tolerance': total_tolerance})
    print table[best_k]

    print "best tolerance:"
    print round(table[best_k][0],4)
    print "best k:"
    print round(table[best_k][1],4)
    
    result_groups =  classificator.variation_classifier(mix, round(table[best_k][0],4), print_value, 0)
    if(print_value > 0):
        result_splited = classificator.print_groups(result_groups)

    #merge:
    #print merge(mix, result_splited)
    
    fig = plt.figure()
    plot(total_tolerance,total_sse, "SSE", "Tolerance")
    plot(total_tolerance,total_groups, "N Groups", "Tolerance")

    return result_groups

def test2():
    print "Test 2"
    ok = Gauss(200, 50).gen_samples(1000, 0)
    bad = Gauss(800, 50).gen_samples(100, 1)
    
    mix = pd.concat([ok, bad], ignore_index=True)
    
    classificator = Classification()
    i = 0.1

    table = []
    total_groups = []
    total_sse = []
    total_tolerance = []
    
    while i < 2.0:
        print "Classification"
        result_groups =  classificator.variation_classifier(mix, i, 0)
        #print result_groups
        result_sse = classificator.calculate_SSE(result_groups, len(result_groups), 0)
        print result_sse
        i+=0.1
        hash_tolerance_SSE = []
        hash_tolerance_SSE.append(i)
        hash_tolerance_SSE.append(len(result_groups))
        hash_tolerance_SSE.append(result_sse)

        total_groups.append(len(result_groups))
        total_sse.append(result_sse)
        total_tolerance.append(i)
        
        table.append(hash_tolerance_SSE)
    print table
    
    best_k = classificator.best_k({'n_groups': total_groups, 'sse': total_sse, 'tolerance': total_tolerance})
    print table[best_k]

    print "best tolerance:"
    print round(table[best_k][0],4)
    print "best k:"
    print round(table[best_k][1],4)
    
    result_groups =  classificator.variation_classifier(mix, round(table[best_k][0],4), 0)
    classificator.print_groups(result_groups)
    
    fig = plt.figure()
    plot(total_tolerance,total_sse, "SSE", "Tolerance")
    plot(total_tolerance,total_groups, "N Groups", "Tolerance")
    
    #return the results:
    return result_groups
    
    
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

#Plot:
def plot(x, y, labely, labelx):
    #plt.plot([1,2,3,4])
    
    pylab.plot(x, y, '-b', label='sine')
    plt.ylabel(labely)
    plt.xlabel(labelx)
    plt.show()
    
    return plt

#Test number 4:
def test4():
    ok = Gauss(200, 50).gen_samples(1000, 0)
    classifier = Classification()

    test = [764395.0, 7152665.0, 1320533900, 192039500, 2.497488500, 3.092473600, 3.691400500, 4.33296400, 4.930149100, 5.529365300]
    #kmeans(self, n_groups, n_items, numbers):
    result = classifier.kmeans(1, len(test), test)
    print result

def csv_read(position):
    import csv
    #position = 0 
    temp = []
    path = '/home/frank/Desktop/build-trouble-Desktop-Debug/troubleSample.csv'
    with open(path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if(len(row) > position):
                temp.append(int(row[position]))
                
    return temp

def testEachCSVCollumn(col, test, print_flag):
    #classification for first collumn
    read_group1 = csv_read(col)
    print read_group1
    test.append(read_group1)
    
    result = testClassification(read_group1, 0)

    if(print_flag > 0):
        print result
    return result

#This function finds the classification 
def find_group(test, number):

    j = 0
    for each in test:
        i = 0
        while i < len(each):
            if(each[i] == number):
                return j    
            i+=1
        j+=1

#This function connects for each run:
def connect(test):
    "Connect"
    totalRun = []
    position = 0
    while position < 50:
        run = []
        for each in test:
            run.append(each[position])
            
        totalRun.append(run)
        position+=1
    print totalRun

    return totalRun

def testCSV():
    #normal_distribution()
    test = []
    result_classication = []
    
    #Classify:
    result_classication.append(testEachCSVCollumn(1, test, 0))
    result_classication.append(testEachCSVCollumn(2, test, 0))
    result_classication.append(testEachCSVCollumn(3, test, 0))
    result_classication.append(testEachCSVCollumn(4, test, 0))
    
    #Connect with run:
    print result_classication
    result = connect(test)
    #show the classification:
    
def main():
    #testCSV()
    result = find_group([[1,2,4,5,6],[3,4,5,6]],4)
    print result
    
if __name__ == '__main__':
    main()
