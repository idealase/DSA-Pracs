#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

my_list = [29, 5, 18, 13, 12, 20, 50, 214, 1]
verbose_output = True


def bubble_sort(input_array):
    pass_num = 0
    is_sorted = False

    while not is_sorted:
        is_sorted = True   # assume sorted - we'll find out if its not
        for i in range(0, (len(input_array) - 1 - pass_num)):
            if input_array[i] > input_array[i + 1]:
                prev_array = input_array.copy()
                temp = input_array[i]     # swap elements i and i+1
                input_array[i] = input_array[i + 1]
                input_array[i + 1] = temp
                is_sorted = False  # still need to continue sorting
                if verbose_output:
                    print("On Pass " + str(pass_num+1) + ": Swapped " +
                          str(input_array[i+1]) + " with " +
                          str(input_array[i]))
                    print(str(prev_array) + " -----> " +
                          str(input_array) + "\n")
        pass_num += 1
    print("Sorted list: " + str(input_array))
        

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


