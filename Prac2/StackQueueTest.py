import myStack
import myQueue
import random
import reporting

# init stack
my_stack = myStack.DSAStack(100)

# put 99 values on the stack
for i in range(0, 99):
    value = random.randint(0, 100)
    my_stack.push(value)

# see the top value
top_val = my_stack.top()
print("The top value in your stack is " + str(top_val))
print("There are " + str(my_stack.count) + " items in the stack")

# push another value, reaching stack limit
value = random.randint(0, 100)
print("Attempting to push " + str(value) + " to stack")
my_stack.push(value)
top_val = my_stack.top()
print("The top value in your stack is " + str(top_val))
print("There are " + str(my_stack.count) + " items in the stack")

# push another value, beyond limit
value = random.randint(0, 100)
print("Attempting to push " + str(value) + " to stack")
my_stack.push(value)
top_val = my_stack.top()
print("The top value in your stack is " + str(top_val))
print("There are " + str(my_stack.count) + " items in the stack")

# init queue
my_queue = myQueue.DSAQueue()

# enqueue 100 items
for i in range(0, 100):
    value = random.randint(0, 100)
    my_queue.enqueue(value)

# look at first in queue
peekd_val = my_queue.peek()
print("\nThe peeked value in your queue is " + str(peekd_val))
print("There are " + str(my_queue.count) + " items in the queue")

# attempt to enqueue another value, beyond limit
value = random.randint(0, 100)
my_queue.enqueue(value)
peekd_val = my_queue.peek()
print("The peeked value in your queue is " + str(peekd_val))
print("There are " + str(my_queue.count) + " items in the queue")

reporting.gen_report()
