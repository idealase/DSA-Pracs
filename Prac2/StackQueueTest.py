import myStack
import myQueue
import random
import reporting

my_stack = myStack.DSAStack(99)

for i in range(0, 99):
    value = random.randint(0, 100)
    my_stack.push(value)

top_val = my_stack.top()

print(top_val)

my_queue = myQueue.DSAQueue()

for i in range(0, 99):
    value = random.randint(0, 100)
    my_queue.enqueue(value)

peekd_val = my_queue.peek()
print(peekd_val)


reporting.gen_report()
