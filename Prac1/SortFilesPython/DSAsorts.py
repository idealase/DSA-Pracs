#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

my_list = [29, 5, 18, 13, 12, 20, 50, 214, 1]


def bubble_sort(input_array):
    passno = 0
    sorted = False

    while not sorted:
        sorted = True   # assume sorted - we'll find out if its not
        for i in range(0, (len(input_array) - 1 - passno)):
            if input_array[i] > input_array[i + 1]:
                previousA = input_array   # FIXME: not assigning correctly
                temp = input_array[i]     # swap elements i and i+1
                input_array[i] = input_array[i + 1]
                input_array[i + 1] = temp
                sorted = False  # still need to continue sorting
                print("On Pass " + str(passno+1) + ": Swapped " + str(input_array[i]) +
                      " with " + str(input_array[i + 1]))
                print(str(previousA) + " became " + str(input_array) + "\n")
        passno += 1
        

bubble_sort(my_list)











def insertionSort(A):
    ...

def selectionSort(A):
    ...

def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    ...

def mergeSortRecurse(A, leftIdx, rightIdx):
    ...

def merge(A, leftIdx, midIdx, rightIdx):
    ...

def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...

def quickSortRecurse(A, leftIdx, rightIdx):
    ...

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    ...


