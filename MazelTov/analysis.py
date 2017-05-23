#This part of the program do the analysis of the tree
#basically by creating a tree graph in a file
from node import *
from reader import *

#Imports
import graphviz as gv
import csv

#Class to do the analysis
class Analysis(object):
    def __init__(self, tree):
        self.tree = tree

    "This function will create a file with the tree"
    def create_graph(self):

        return 0

    "This function will create the json for the tree"
    def create_json(self):
        return 0

    "This function will analyze the metrics in the nodes"
    def analyze_metrics(self):
        return 0

    "This function will create a csv file with the metrics"
    def create_csv(self):
        with open('tree.csv', 'wb') as f:
            writer = csv.writer(f)
            writer.writerows(someiterable)

    "This function will do the inorder traversal"
    def traversal(self, full):
        self.get_data(self.tree, full)
        return full

    "Inorder traversal + visitor:Q" \
    ""
    def get_data(self, node, full):
        list = node.get_children()
        print (node.get_label())
        full.append(node.get_label())
        i = 0
        while i < len(list):
            self.get_data(list[i], full)
            i = i + 1
