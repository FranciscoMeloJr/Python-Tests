"This function will do the automated classification"

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


"Gauss classification"
class Gauss(object):
    def __init__(self, mean=0, stddev=1):
        self.mean = mean
        self.stddev = stddev

    def gen_samples(self, n, tag=0):
        samples = self.stddev * np.random.randn(n) + self.mean;
        guess = tag
        return pd.DataFrame({'tag': tag, 'samples': samples, 'guess': guess})

"Class for classification"
class Classification(object):
    """ Constructor for the Classification class: """

    def __init__(self):
        print
        'Constructor'

    "Range classifier =[[1,2,3,1,2,3]]"
    def range_classifier(self, data, range, flag = True):

        if(flag):
            print data
        data = sorted(data)
        max = len(data)/range

        if (flag):
            print data

        temp = []
        total = []
        j = 0
        if (flag):
            print max

        for each in data:
            each = float(each
                         )
            if (j < max):
                temp.append(each)
                j+=1
            else:
                total.append(temp)
                temp = []
                temp.append(each)
                j = 0


        total.append(temp)
        return total

    """ This function calculates the difference of a number in a list:"""
    def calculate_difference(self, data, flag_print, kind):
        # print 'calculate difference'
        result = []
        original = data
        ordered = data.sort()

        i = 1
        # it is a list:
        if (kind > 0):
            list_data = data['samples']
        else:
            list_data = data
        list_difference = []

        # calculate the difference:
        for i in range(len(list_data)):
            # print list_data[i]
            list_difference.append(int(list_data[i]) - int(list_data[i - 1]))

        if (flag_print > 0):
            print
            len(list_difference)

        i = 0
        total_difference = 0
        for i in range(len(list_difference)):
            total_difference += list_difference[i]

        # mean:
        if (len(list_difference) != 0):
            total_difference /= len(list_difference)
        else:
            total_difference = 0

        return total_difference

    """ Jenks Natural Breaks"""
    def jnb_classifier(self, p_data, natural_breaks = 2, print_flag = False, plot_flag = False):
        data = []
        for each in p_data:
            data.append(int(each))

        data = sorted(data)
        print data
        diff_list = []
        i = 1

        diff_list = self.calculate_diff(data)

        #iterating over the diff_list:
        max = []
        max.append(self.take_max(diff_list))
        if(print_flag):
            print "diff list " + str(diff_list)
            print "max " + str(max)

        j = 0
        while j < (natural_breaks - 2 ):
            diff_list.remove(max[j])
            max.append(self.take_max(diff_list))
            j+=1

        result = self.divide_data(max, data)

        # for each in result:
        #     diff_list = self.calculate_diff(each)
        #     print "each diff " + str(diff_list)
        #     print "max" + str(self.take_max(diff_list))
        #
        # print result

        if(print_flag):
            print "result" + str(result)
        return result

    "This function does the division taking the two borders"
    def divide_data(self, max, data):

        i = 0
        result = []
        groups = []
        splits = []
        for eachM in max:
            splits.append(eachM[2])

        splits = sorted(splits)

        i = 0
        j = 0
        while j < len(splits):
            while i <= splits[j]:
                each = data[i]
                groups.append(each)
                i += 1

            result.append(groups)
            groups = []
            j +=1

        while i < len(data):
            each = data[i]
            groups.append(each)
            i += 1
        result.append(groups)

        return result
    "This function calculates the diff"
    def calculate_diff(self, data):
        i = 1
        diff_list = []
        while i < len(data):
            each = data[i]
            previous = data[i-1]
            diff = each - previous
            diff_list.append([diff, i, i-1])
            i +=1
        return diff_list

    "This function takes the maximum value a list inside a tuple (JNB II)"
    def take_max(self, diff_list):
        max = diff_list[0]
        i = 0
        # finding the biggest gap:
        while i < len(diff_list):
            each = diff_list[i]
            if (each[0] > max[0]):
                max = each
            i += 1

        return max

    """ Variation classification: algorithm using tolerance"""
    def variation_classifier(self, data, tolerance, print_flag, kind):

        # mean distance:
        mean_difference = self.calculate_difference(data, 0, kind)
        if (kind > 0):
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
        if (print_flag > 0):
            debug(xis)

        previous = int(xis[0])
        mini_groups = []
        result = []
        if (print_flag > 0):
            print
            'Variation classification tolerance'
            print
            self.valid_numbers(xis)

        # tolerance = 0.5
        for i in range(len(xis)):
            temp = float(xis[i])
            if (print_flag > 0):
                print
                "Value and group"
                print
                temp
                print
                len(result)
            # if(temp > previous +(previous * tolerance)):
            comp = float(previous) + (float(previous) / tolerance)
            if (temp > comp):
                result.append(mini_groups)
                mini_groups = []
            mini_groups.append(temp)
            previous = float(temp)
        result.append(mini_groups)

        if (print_flag > 0):
            print
            'Number of groups:'
            print
            len(result)
            print
            result

        return result

    """ Function to calcualte the SSE, used for the Elbow method: """

    def calculate_SSE(self, list_groups, n_groups, flag_print):
        # list_groups[[1,2,3],[4,5,6]]
        centroids = []
        i = 0
        while i < len(list_groups):
            temp = list_groups[i]
            if (len(temp) > 0):
                j = 0
                aux = 0
                while j < len(temp):
                    aux += temp[j]
                    j += 1
                centroids.append(aux / j)
            else:
                centroids.append(0)
            i += 1
        if (flag_print > 0):
            print
            len(centroids)
            print
            "Centroid size", centroids
            print
            "Groups qtd", len(list_groups)
        # SSE Calculation:
        SSE = 0
        i = 0
        k = 0
        for i in range(len(list_groups)):
            x = list_groups[i]
            if (len(x) > 0):
                if (flag_print > 0):
                    print
                    x
                j = 0
                for j in range(len(x)):
                    eachDistance = (x[j] - centroids[i]) * (x[j] - centroids[i])
                    SSE += eachDistance
                    j += 1

        return SSE

    """ Heuristic to evaluate the method """

    def best_k(self, dic):
        list_groups = []
        group1 = []
        list_groups.append(group1)

        # {'n_groups': total_groups, 'sse': total_sse, 'tolerance': total_tolerance})
        n_groups = dic['n_groups']
        tolerance = dic['tolerance']
        calculated_SSE = dic['sse']
        maxp1 = 0
        minp1 = 0

        i = 1
        gap = 0
        for i in range(len(calculated_SSE)):
            current = calculated_SSE[i - 1] - calculated_SSE[i]
            if (current > gap):
                gap = current
                maxp1 = i

        gap = 0
        i = 1
        for i in range(len(calculated_SSE)):
            current = calculated_SSE[i - 1] - calculated_SSE[i]
            if (current < gap):
                gap = current
                minp1 = i

        # return minp1
        # return {'b_n_groups': n_groups[maxp1],'b_tolerance': tolerance[maxp1], 'b_sse': calculated_SSE[maxp1]}
        return maxp1


    """ This is the opt_kmeans, which takes the k_means and apply: """
    def Opk_means(self, data):
        elbow = []
        elbow.append(k_means(data, k))

    def print_groups(self, data):
        i = 0
        groups = []
        numbers = []
        for i in range(len(data)):
            j = 0
            temp = data[i]
            for j in range(len(temp)):
                print
                '{0:2f} {1:3d}'.format(temp[j], i + 1)
                groups.append(i + 1)
                numbers.append(temp[j])
        return {'result': numbers, 'guess': groups}

    # validating the sort:
    def valid_numbers(self, data):
        i = 1
        while i < len(data):
            if (data[i - 1] > data[i]):
                return False
            i += 1
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
            i += 1
        pdb.set_trace()
        dataItemsD = numbers
        i = 0
        while i < len(dataItemsD):
            if (i < k1):
                czD.append(dataItemsD[i])
            i += 1
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
                if (ite == i):
                    oldCzD.append(czD[i])
                else:
                    oldCzD.insert(i, czD[i])
                if ((len(groupsD[i]) > 0)):
                    czD.insert(i, self.averageD(groupsD[i]));
                i += 1
            if (self.equals(czD, oldCzD) == False):
                j = 0
                while j < len(groupsD):
                    groupsD[j] = []
                    j += 1
                i += 1
            ite += 1
            if (self.equals(czD, oldCzD) == False):
                break

        return groupsD;

    # calculate the average:
    def averageD(self, list_n):
        sum = 0.0;
        i = 0
        for i in range(len(list_n)):
            sum += list_n[i]
        return (sum / len(list_n))

    # equals
    def equals(self, list_x, list_y):
        if (cmp(list_x, list_y) == 0):
            return True
        return False

    # add:
    def add(self, list_a, index, aItem):
        i = 0

        while i <= index:
            aux = []
            aux.append('')
            list_a.append(aux)
            i += 1

        aux = aItem
        list_a[index] = aux

        return list_a

"Test the JNB classification"
def testClassification_jnb(mix, print_flag, plot_flag):

    classificator = Classification()
    result_groups = classificator.jnb_classifier(mix, n_b, print_flag, plot_flag)




"Test the classification with several groups"
def testClassification(mix, print_flag, plot_flag):
    print
    "Test Classification"
    # mix = pd.concat([ok, bad], ignore_index=True)

    classificator = Classification()
    i = 0.1

    table = []
    total_groups = []
    total_sse = []
    total_tolerance = []

    while i < 20:
        if (print_flag > 0):
            print
            "Classification"
            print
            mix
        result_groups = classificator.variation_classifier(mix, i, print_flag, 0)
        # print result_groups
        result_sse = classificator.calculate_SSE(result_groups, len(result_groups), print_flag)
        # print result_sse
        i += 1
        hash_tolerance_SSE = []
        hash_tolerance_SSE.append(i)
        hash_tolerance_SSE.append(len(result_groups))
        hash_tolerance_SSE.append(result_sse)

        total_groups.append(len(result_groups))
        total_sse.append(result_sse)
        total_tolerance.append(i)

        table.append(hash_tolerance_SSE)
    print
    table

    best_k = classificator.best_k({'n_groups': total_groups, 'sse': total_sse, 'tolerance': total_tolerance})
    print
    table[best_k]

    print
    "best tolerance:"
    print
    round(table[best_k][0], 4)
    print
    "best k:"
    print
    round(table[best_k][1], 4)

    result_groups = classificator.variation_classifier(mix, round(table[best_k][0], 4), print_flag, 0)
    if (print_flag > 0):
        result_splited = classificator.print_groups(result_groups)

    # merge:
    # print merge(mix, result_splited)

    if (plot_flag > 0):
        fig = plt.figure()
        plot(total_tolerance, total_sse, "SSE", "Tolerance")
        plot(total_tolerance, total_groups, "N Groups", "Tolerance")

    return result_groups


"Test for classification"
def test():
    # simulation()
    ok = Gauss(200, 50).gen_samples(1000, 0)
    classificator = Classification()
    i = 0

    table = []
    total_groups = []
    total_sse = []
    total_tolerance = []
    print_value = 0
    while i < 3.0:
        if (print_value > 0):
            print
            "Classification"
        result_groups = classificator.variation_classifier(ok, i, print_value, 0)
        # print result_groups
        result_sse = classificator.calculate_SSE(result_groups, len(result_groups), print_value)
        print
        result_sse
        i += 0.1
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
    plot(total_tolerance, total_sse, "SSE", "Tolerance")
    plot(total_tolerance, total_groups, "N Groups", "Tolerance")

"Test 2"
def test2():
    print
    "Test 2"
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
        print
        "Classification"
        result_groups = classificator.variation_classifier(mix, i, 0)
        # print result_groups
        result_sse = classificator.calculate_SSE(result_groups, len(result_groups), 0)
        print
        result_sse
        i += 0.1
        hash_tolerance_SSE = []
        hash_tolerance_SSE.append(i)
        hash_tolerance_SSE.append(len(result_groups))
        hash_tolerance_SSE.append(result_sse)

        total_groups.append(len(result_groups))
        total_sse.append(result_sse)
        total_tolerance.append(i)

        table.append(hash_tolerance_SSE)
    print
    table

    best_k = classificator.best_k({'n_groups': total_groups, 'sse': total_sse, 'tolerance': total_tolerance})
    print
    table[best_k]

    print
    "best tolerance:"
    print
    round(table[best_k][0], 4)
    print
    "best k:"
    print
    round(table[best_k][1], 4)

    result_groups = classificator.variation_classifier(mix, round(table[best_k][0], 4), 0)
    classificator.print_groups(result_groups)

    fig = plt.figure()
    plot(total_tolerance, total_sse, "SSE", "Tolerance")
    plot(total_tolerance, total_groups, "N Groups", "Tolerance")

    # return the results:
    return result_groups

"Test 3"
def test3():
    print
    "Test 3"
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
        if (print_value > 0):
            print
            "Classification"
        result_groups = classificator.variation_classifier(mix, i, print_value, 1)
        # print result_groups
        result_sse = classificator.calculate_SSE(result_groups, len(result_groups), print_value)
        # print result_sse
        i += 1
        hash_tolerance_SSE = []
        hash_tolerance_SSE.append(i)
        hash_tolerance_SSE.append(len(result_groups))
        hash_tolerance_SSE.append(result_sse)

        total_groups.append(len(result_groups))
        total_sse.append(result_sse)
        total_tolerance.append(i)

        table.append(hash_tolerance_SSE)
    print
    table

    best_k = classificator.best_k({'n_groups': total_groups, 'sse': total_sse, 'tolerance': total_tolerance})
    print
    table[best_k]

    print
    "best tolerance:"
    print
    round(table[best_k][0], 4)
    print
    "best k:"
    print
    round(table[best_k][1], 4)

    result_groups = classificator.variation_classifier(mix, round(table[best_k][0], 4), 0, 1)
    result_splited = classificator.print_groups(result_groups)

    # merge:
    # print merge(mix, result_splited)

    fig = plt.figure()
    plot(total_tolerance, total_sse, "SSE", "Tolerance")
    plot(total_tolerance, total_groups, "N Groups", "Tolerance")

    return result_groups


"This function will do the automated classification"
def testClassification(mix, print_flag, plot_flag):
    print
    "Test Classification"
    # mix = pd.concat([ok, bad], ignore_index=True)

    classificator = Classification()
    i = 0.1

    table = []
    total_groups = []
    total_sse = []
    total_tolerance = []

    passo = 5
    while i < 200:
        if (print_flag > 0):
            print
            "Classification"
            print
            mix
        # (self, data, tolerance, print_flag, kind):
        result_groups = classificator.variation_classifier(mix, i, print_flag, 0)
        # print result_groups
        result_sse = classificator.calculate_SSE(result_groups, len(result_groups), print_flag)
        # print result_sse
        i += passo
        hash_tolerance_SSE = []
        hash_tolerance_SSE.append(i)
        hash_tolerance_SSE.append(len(result_groups))
        hash_tolerance_SSE.append(result_sse)

        total_groups.append(len(result_groups))
        total_sse.append(result_sse)
        total_tolerance.append(i)

        table.append(hash_tolerance_SSE)
    print
    table

    best_k = classificator.best_k({'n_groups': total_groups, 'sse': total_sse, 'tolerance': total_tolerance})
    print
    table[best_k]

    print
    "best tolerance:"
    print
    round(table[best_k][0], 4)
    print
    "best k:"
    print
    round(table[best_k][1], 4)

    result_groups = classificator.variation_classifier(mix, round(table[best_k][0], 4), print_flag, 0)
    if (print_flag > 0):
        result_splited = classificator.print_groups(result_groups)

    # merge:
    # print merge(mix, result_splited)

    if (plot_flag > 0):
        fig = plt.figure()
        plot(total_tolerance, total_sse, "SSE", "Tolerance")
        plot(total_tolerance, total_groups, "N Groups", "Tolerance")

    return result_groups

"This function will do the automated classification"
def testClassification_specific_range(mix, groups, print_flag = False, plot_flag = False):
    print "Test Classification"

    classificator = Classification()

    table = []
    total_groups = []
    total_sse = []
    total_tolerance = []

    # (self, data, tolerance, print_flag, kind):
    result_groups = classificator.jnb_classifier(mix, groups, print_flag, plot_flag)

    print result_groups
    return result_groups

"This function will do the automated classification"
def testClassification_range(mix, print_flag, plot_flag):
    print
    "Test Classification"
    # mix = pd.concat([ok, bad], ignore_index=True)

    classificator = Classification()
    i = 2

    table = []
    total_groups = []
    total_sse = []
    total_tolerance = []

    passo = 5
    while i < 100:
        if (print_flag > 0):
            print
            "Classification"
            print
            mix
        # (self, data, tolerance, print_flag, kind):
        result_groups = classificator.range_classifier(mix, i, print_flag)
        print "xxxxx"
        print result_groups
        # print result_groups
        result_sse = classificator.calculate_SSE(result_groups, len(result_groups), print_flag)
        # print result_sse
        i += passo
        hash_tolerance_SSE = []
        hash_tolerance_SSE.append(i)
        hash_tolerance_SSE.append(len(result_groups))
        hash_tolerance_SSE.append(result_sse)

        total_groups.append(len(result_groups))
        total_sse.append(result_sse)
        total_tolerance.append(i)

        table.append(hash_tolerance_SSE)
    print
    table

    best_k = classificator.best_k({'n_groups': total_groups, 'sse': total_sse, 'tolerance': total_tolerance})
    print
    table[best_k]

    print
    "best tolerance:"
    print
    round(table[best_k][0], 4)
    print
    "best k:"
    print
    round(table[best_k][1], 4)

    result_groups = classificator.variation_classifier(mix, round(table[best_k][0], 4), print_flag, 0)
    if (print_flag > 0):
        result_splited = classificator.print_groups(result_groups)

    # merge:
    # print merge(mix, result_splited)

    if (plot_flag > 0):
        fig = plt.figure()
        plot(total_tolerance, total_sse, "SSE", "Tolerance")
        plot(total_tolerance, total_groups, "N Groups", "Tolerance")

    return result_groups
"Test number 4"
def test4():
    ok = Gauss(200, 50).gen_samples(1000, 0)
    classifier = Classification()

    test = [764395.0, 7152665.0, 1320533900, 192039500, 2.497488500, 3.092473600, 3.691400500, 4.33296400, 4.930149100, 5.529365300]
    #kmeans(self, n_groups, n_items, numbers):
    result = classifier.kmeans(1, len(test), test)
    print result

"Test number 5 - this function test the division with specific groups, example: 3 = [][][]"
def test5():
    classifier = Classification()

    test = [764395.0, 7152665.0, 1320533900, 192039500, 2.497488500, 3.092473600, 3.691400500, 4.33296400, 4.930149100, 5.529365300]
    #kmeans(self, n_groups, n_items, numbers):
    result = classifier.range_classifier(test, 3)
    print result


"Test number 6 - This function test the JNB"
def test6():
    classifier = Classification()

    testData = [1000,1001,999,10,11,12,13,14,50,51,52,53]
    #test = [1001,1000,10,11,12,13]
    #kmeans(self, n_groups, n_items, numbers):
    result = classifier.jnb_classifier(testData, 3)
    print result

"Function to test CSV"
def testCSV():
    # normal_distribution()
    test = []
    groups_classification = []

    # Classify:
    groups_classification.append(testEachCSVCollumn(0, test, 0, 0))
    groups_classification.append(testEachCSVCollumn(1, test, 0, 0))
    groups_classification.append(testEachCSVCollumn(2, test, 0, 0))
    groups_classification.append(testEachCSVCollumn(3, test, 0, 0))
    groups_classification.append(testEachCSVCollumn(4, test, 0, 0))

    # Connect with run:
    result = connect(test, 0)

    # [[[1, 2, 4, 5, 6], [3, 4, 5, 6]], [[0, 2, 4, 5, 6], [3, 3, 5, 8]]]
    classification_result = classify_each_run(result, groups_classification, 0)

    # show the classification:
    create_runs(result, classification_result, 1)


    # return list_runs
"Main function"
def main():
    test6()


# main()
