#!/usr/bin/python3
'''
Created on Nov 1, 2016

@author: francis with changes of Francisco
'''
import urllib

def request():
    localhost = urllib.urlopen("http://localhost:8280/")
    print localhost.read(100)
       
#Main function to test all:
def main():
    #testCSV()
    request()
    
if __name__ == '__main__':
    main()
