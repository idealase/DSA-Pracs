#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

my_list = [29, 5, 18, 13, 12, 20, 50, 214, 1]
verbose_output = True


def bubble_sort(array):
    pass_num = 0
    is_sorted = False

    while not is_sorted:
        is_sorted = True   # assume sorted - we'll find out if its not
        for i in range(0, (len(array) - 1 - pass_num)):
            if array[i] > array[i + 1]:
                prev_array = array.copy()
                temp = array[i]     # swap elements i and i+1
                array[i] = array[i + 1]
                array[i + 1] = temp
                is_sorted = False  # still need to continue sorting
                if verbose_output:
                    print("On Pass " + str(pass_num+1) + ": Swapped " +
                          str(array[i + 1]) + " with " +
                          str(array[i]))
                    print(str(prev_array) + " -----> " +
                          str(array) + "\n")
        pass_num += 1
    print("Sorted list: " + str(array))


def insertion_sort(array):
    ...


def selection_sort(array):
    for i in range(0, (len(array)-1)):
        min_idx = i
        for j in range((i+1), len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        prev_array = array.copy()
        temp = array[min_idx]
        array[min_idx] = array[i]
        array[i] = temp
        if verbose_output:
            print(str(prev_array) + " -----> " + str(array))

    print("Sorted list: " + str(array))


def merge_sort(array):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    ...


def merge_sort_recurse(array, leftIdx, rightIdx):
    ...


def merge(array, leftIdx, midIdx, rightIdx):
    ...


def quick_sort(array):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...


def quick_sort_recurse(array, leftIdx, rightIdx):
    ...


def do_partitioning(array, leftIdx, rightIdx, pivotIdx):
    ...


# bubble_sort(my_list)
selection_sort(my_list)
