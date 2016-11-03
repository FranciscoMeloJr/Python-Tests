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

class Gauss(object):
    def __init__(self, mean=0, stddev=1):
        self.mean = mean
        self.stddev = stddev
        
    def gen_samples(self, n, tag=0):
        samples = self.stddev * np.random.randn(n) + self.mean;
        #return pd.DataFrame({'tag': tag, 'samples': samples})
        guess = tag
        return pd.DataFrame({'tag': tag, 'samples': samples, 'guess': guess})

class Classification(object):
    """ Constructor for the Classification class: """
    def __init__(self):
        print 'Constructor'

    """ This function calculates the difference of a number in a list:"""
    def calculate_difference(self, data, flag_print):
        #print 'calculate difference'
        result = []
        original = data
        ordered = data.sort()

        i = 1
        #it is a list:
        list_data = data['samples']
        list_difference = []

        #calculate the difference:
        while i < len(list_data):
            #print list_data[i]
            list_difference.append(list_data[i] - list_data[i-1])
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
    def variation_classifier(self, data, tolerance, print_flag):
        print 'Variation classification'
        #mean distance:
        mean_difference = self.calculate_difference(data, 0)
        list_data = data['samples']
        list_sorted = list_data.copy()
        list_sorted.sort()
        i = 1
        previous = list_data[0]
        mini_groups = []
        result = []
        #tolerance = 0.5
        while i < len(list_data):
            temp = list_data[i]
            if(temp > previous +(previous / tolerance)):
                result.append(mini_groups)
                mini_groups = []
            mini_groups.append(temp)
            previous = temp
            i+=1
        result.append(mini_groups)

        print 'Number of groups:'
        print len(result)
        if(print_flag>0):
            print result

        return result

    """ Function to calcualte the SSE, used for the Elbow method: """    
    def calculate_SSE(self, list_groups, n_groups):
        #list_groups[[1,2,3],[4,5,6]]
        centroids = []
        i = 0
        while i < len(list_groups):
            temp = list_groups[i]
            j = 0
            aux = 0
            while j < len(temp):
                aux += temp[j]
                j+=1
            centroids.append(aux/j)
            i+=1
        #print len(centroids)
        #SSE Calculation:
        SSE = 0
        i = 0 
        while i < len(list_groups):
             x = list_groups[i]  
             j = 0
             while j < len(x):
                 eachDistance = (x[j] - centroids[i]) * (x[j] - centroids[i])
                 SSE += eachDistance
                 j+=1
             i+=1
        return SSE

    """ Heuristic to evaluate the method """
    def best_k(self, list_groups):
        list_groups = []
        group1 = []
        list_groups.append(group1)
        
        self.calculate_SSE(list_groups)
        
    """ // Heuristic to get the best k: maximum gap distance
    public static int calculateBestK(ArrayList<Double> resultSSE) {

        Double gap = (double) 0;
        Double current;
        int maxp1 = 0;
        int minp1 = 0;
        int i;

        // Heuristic max:
        for (i = 1; i < resultSSE.size(); i++) {
            current = resultSSE.get(i - 1) - resultSSE.get(i);
            if (current > gap) {
                gap = current;
                maxp1 = i;
            }
        }
        // Heuristic min:
        gap = (double) 0;
        for (i = 1; i < resultSSE.size(); i++) {
            current = resultSSE.get(i - 1) - resultSSE.get(i);
            if (current < gap) {
                gap = current;
                minp1 = i;
            }
        }
        // return minp1;

        System.out.println("best k " + maxp1);
        //return minp1;
        return maxp1;
    }"""
        
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

def test():
    #simulation()
    ok = Gauss(200, 50).gen_samples(1000, 0)
    classificator = Classification()
    i = 0

    table = []
    total_groups = []
    total_sse = []
    total_tolerance = []
    
    while i < 1.0:
        print "Classification"
        result_groups =  classificator.variation_classifier(ok, i, 0)
        #print result_groups
        result_sse = classificator.calculate_SSE(result_groups, len(result_groups))
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
    
    fig = plt.figure()
    plot(total_tolerance,total_sse, "SSE", "Tolerance")
    plot(total_tolerance,total_groups, "N Groups", "Tolerance")
    
    
def simulation():
    ok = Gauss(200, 50).gen_samples(1000, 0)
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

    return ok

def plot(x, y, labely, labelx):
    #plt.plot([1,2,3,4])
    
    pylab.plot(x, y, '-b', label='sine')
    plt.ylabel(labely)
    plt.xlabel(labelx)
    plt.show()
    
    return plt
    
def main():
    #simulation()
    test()
    
if __name__ == '__main__':
    main()
