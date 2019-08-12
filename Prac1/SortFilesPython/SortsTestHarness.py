"""
Testharness to generate various different types of arrays of integers
and then sort them using various sorts.

Each sort is run REPEATS times, with the first result discarded,
and the last REPEATS-1 runs averaged to give the running time.

-------------------------------------------------------------

Author of java version: Andrew Turpin (andrew@cs.curtin.edu.au)
Date:    August 2004
Modified (java): Patrick Peursum
Date:     Sep 2009
Modified (python): Valerie Maxville
Date:    August 2017
Modified (python): Hayden Richards
Date:    March 2018
Modified (python): Brodie Sandford
Date: August 2019
"""

import numpy as np
import sys
import timeit
import DSAsorts
import random


REPEATS = 3              # No times to run sorts to get mean time
NEARLY_PERCENT = 0.10    # % of items to move in nearly sorted array
RANDOM_TIMES = 100       # No times to randomly swap elements in array


def usage():
    print(" Usage: python SortsTestHarness.py n xy [xy ...]")
    print("        where")
    print("        n is number of integers to sort")
    print("        x is one of")
    print("           b - bubblesort")
    print("           i - insertion sort")
    print("           s - selection sort")
    print("           q - quicksort")
    print("           m - mergesort")
    print("        y is one of")
    print("           a - 1..n ascending")
    print("           d - 1..n descending")
    print("           r - 1..n in random order")
    print("           n - 1..n nearly sorted (10% moved)")


def do_sort(n, sortType, arrayType):
        array = np.arange(1, n+1, 1)   # array w/ values from 1 to n
        
        if arrayType == 'a':
            print("Ascending: ", array)
        elif arrayType == 'd':  # convert to descending
            for i in range(0, int(n/2)):
                temp = array[i]
                array[i] = array[n-i-1]
                array[n-i-1] = temp
            print("Descending: ", array)
        elif arrayType == 'r':
            for i in range(RANDOM_TIMES*n):
                x = int(random.random()*n)
                y = int(random.random()*n)
                temp = array[x]
                array[x] = array[y]
                array[y] = temp
            print("Random: ", array)
        elif arrayType == 'n':
            for i in range(int(n*NEARLY_PERCENT/2+1)):
                x = int(random.random()*n)
                y = int(random.random()*n)
                temp = array[x]
                array[x] = array[y]
                array[y] = temp
            print("Nearly sorted: ", array)
        else:
            print("Unsupported array type")

        if sortType == "b":
            DSAsorts.bubble_sort(array)
        elif sortType == "s":
            DSAsorts.selection_sort(array)
        elif sortType == "i":
            DSAsorts.insertion_sort(array)
        elif sortType == "m":
            DSAsorts.merge_sort(array)
        elif sortType == "q":
            DSAsorts.quick_sort(array)
        else:
            print("Unsupported sort algorithm")

        for i in range(n-2):
            if array[i] > array[i+1]:
                raise ValueError("Array not in order")

# main program


print("\n")

if len(sys.argv) < 3:
    usage()
else:
    for aa in range(2, len(sys.argv)):
        
        n = int(sys.argv[1])
        sort_type = sys.argv[aa][0]
        array_type = sys.argv[aa][1]

        runningTotal = 0

        for repeat in range(REPEATS):
            startTime = timeit.default_timer()
            do_sort(n, sort_type, array_type)
            endTime = timeit.default_timer()

            runningTotal += (endTime - startTime)
    
        print(sort_type + array_type + " " + str(n) + " " +
              str(runningTotal / (REPEATS - 1)))
