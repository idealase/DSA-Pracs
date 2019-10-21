import myStack
import myQueue
import random
import reporting


numPassed = 0
numTests = 0

# TEST 1
# init stack
print("\nTest 1:", end=" ")
try:
    numTests += 1
    my_stack = myStack.DSAStack(100)
    print("Initialised empty stack w/ capacity 100")
    numPassed += 1
except:
    print("Failed")

# TEST 2
# put 99 values on the stack
print("\nTest 2:", end=" ")
try:
    numTests += 1
    for i in range(0, 99):
        value = random.randint(0, 100)
        my_stack.push(value)
    print("Pushed 99 values to stack")
    numPassed += 1
except:
    print("Failed")

# TEST 3
# see the top value
print("\nTest 3:", end=" ")
try:
    numTests += 1
    top_val = my_stack.top()
    print("The top value in your stack is " + str(top_val))
    print("There are " + str(my_stack.count) + " items in the stack")
    numPassed += 1
except:
    print("Failed")

# TEST 4
# push another value, reaching stack limit
print("\nTest 4:", end=" ")
try:
    numTests += 1
    value = random.randint(0, 100)
    print("Attempting to push " + str(value) + " to stack")
    my_stack.push(value)
    top_val = my_stack.top()
    print("The top value in your stack is " + str(top_val))
    print("There are " + str(my_stack.count) + " items in the stack")
    numPassed += 1
except:
    print("Failed")

# TEST 5
# push another value, beyond limit
print("\nTest 5:", end=" ")
try:
    numTests += 1
    value = random.randint(0, 100)
    print("Attempting to push " + str(value) + " to stack")
    my_stack.push(value)
    top_val = my_stack.top()
    print("The top value in your stack is " + str(top_val))
    print("There are " + str(my_stack.count) + " items in the stack")
    numPassed += 1
except:
    print("Failed")

# TEST 6
# init queue
print("\nTest 6:", end=" ")
try:
    numTests += 1
    my_queue = myQueue.DSAQueue()
    print("Initialised empty queue")
    numPassed += 1
except:
    print("Failed")

# TEST 7
# enqueue 100 items
print("\nTest 7:", end=" ")
try:
    numTests += 1
    for i in range(0, 100):
        value = random.randint(0, 100)
        my_queue.enqueue(value)
    numPassed += 1
except:
    print("Failed")

# TEST 8
# look at first in queue
print("\nTest 8:", end=" ")
try:
    numTests += 1
    peekd_val = my_queue.peek()
    print("\nThe peeked value in your queue is " + str(peekd_val))
    print("There are " + str(my_queue.count) + " items in the queue")
    numPassed += 1
except:
    print("Failed")

# TEST 9
# attempt to enqueue another value, beyond limit
print("\nTest 9:", end=" ")
try:
    numTests += 1
    value = random.randint(0, 100)
    my_queue.enqueue(value)
    peekd_val = my_queue.peek()
    print("The peeked value in your queue is " + str(peekd_val))
    print("There are " + str(my_queue.count) + " items in the queue")
    numPassed += 1
except:
    print("Failed")

# Print test summary
print("\nNumber PASSED: ", numPassed, "/", numTests)
print("-> ", numPassed/numTests*100, "%\n")

reporting.gen_report()
