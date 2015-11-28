# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 11:32:17 2015

@author: srini
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 06 20:40:16 2015

@author: srini
"""

from kdtree import KDTree

import csv
import operator


# Function to filter the list
def filter_lambda(filters, tuples):
    return filter(lambda t: all(f(t) for f in filters), tuples)


def nearest_filtered(Primary_Technology, Role):
    #Separating out the indices
    #Opening the files
    
    with open("C:\DataMining\IndexPredictionsOutput.csv", 'rb') as f:
        reader = csv.reader(f)
        data = map(tuple, reader)


    # Filtering the list
    def f1(t): return t[2].strip()==Primary_Technology # Primary Skill is Informatica
    def f2(t): return t[11].strip()==Role # Role

    filters = [f1,f2]    
    
    filtered_data = filter_lambda(filters, data)
    
    
    kd_filtered_data = map(operator.itemgetter(0,58,59,60,61,62,63,64,65,66), filtered_data)


    # Creating the tree

    tree = KDTree.construct_from_data(kd_filtered_data)
 
    # Finding the nearest neighbours, t can be varied for the number of neighbours

    nearest = tree.query(query_point=(85,10,10,10,10,10,10,10,10,10), t=10)

    # The serial number of the nearest neighbours
    nearest_index = [x[0] for x in nearest]

    # Using this to filter the original list
    kd_filtered_nearest = [tup for tup in filtered_data if tup[0] in nearest_index]

    # Preparing the dataset to be printed

    kd_filtered_nearest_printed = map(operator.itemgetter(0,1,2,26,8,23,10), kd_filtered_nearest)

    return kd_filtered_nearest_printed


temp = nearest_filtered("Informatica", "Developer")
print temp
