from myStack import *
from myQueue import *
import random
import reporting

my_stack = DSAStack(99)

for i in range(0, 99):
    value = random.randint(5, 10)
    my_stack.push(value)

top_val = my_stack.top()

print(top_val)

my_queue = DSAQueue()

for i in range(0, 20):
    value = random.randint(0, 10)
    my_queue.enqueue(value)

peekd_val = my_queue.peek()
print(peekd_val)


reporting.gen_report()
