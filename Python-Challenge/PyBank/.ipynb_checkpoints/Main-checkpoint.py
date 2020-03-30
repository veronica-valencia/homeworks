#import Dependencies
import os
#Module for reading CVS files
import csv

#Stores directory name as cwkdir
cwkdir = os.getcwd()

#Joins file path and stores as csvpath
csvpath =  os.path.join( cwkdir,'Python-Challenge','PyBank','Resources', 'budget_data.csv')

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    print (csvreader)

    #reads header for both columns