from heaps import *

numPassed = 0
numTests = 0

# TEST 1
# init heap
print("\nTest 1:", end=" ")
try:
    numTests += 1
    my_heap = DSAHeap(10)
    numPassed += 1
except:
    print("Failed")

# TEST 2
# add to heap
print("\nTest 2:", end=" ")
try:
    numTests += 1
    my_heap.add(50, "Bob")
    my_heap.add(30, "Matt")
    my_heap.add(55, "Mark")
    my_heap.add(70, "Steve")
    numPassed += 1
except:
    print("Failed")



# TEST 3
# remove
print("\nTest 3:", end=" ")
try:
    numTests += 1
    print(my_heap.remove())
    print(my_heap.remove())
    numPassed += 1
except:
    print("Failed")


# Print test summary
print("\n\n\nNumber PASSED: ", numPassed, "/", numTests)
print("-> ", numPassed/numTests*100, "%\n")

