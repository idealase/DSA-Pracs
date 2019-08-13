"""
Activity 2 - Implement Stacks and Queues


DSA Stack
arrays as data structure
"""

import numpy as np


class DSAStack:
    def __init__(self, n=100):
        self.stack = np.empty(n, dtype=object)
        self.count = 0

    def is_full(self):
        """Checks if stack is full"""
        if self.count == len(self.stack):
            return True
        else:
            return False

    def is_empty(self):
        """check if stack is empty"""
        if self.count == 0:
            return True
        else:
            return False

    def push(self, value):
        """add new item to top of stack"""
        if self.is_full():
            print("Stack full")     # FIXME: handle this correctly
            pass
        else:
            self.stack[self.count] = value
            self.count += 1

    def pop(self):
        """take top-most item from stack"""
        if self.is_empty():
            print("Stack empty")  # FIXME: handle this correctly
            pass
        else:
            popped_val = self.stack[self.count]
            del self.stack[self.count]
            self.count -= 1
            return popped_val

    def top(self):
        """look at top-most item, leave it on stack"""
        if self.is_empty():
            print("Stack empty")  # FIXME: handle this correctly
            pass
        else:
            return self.stack[self.count-1]
