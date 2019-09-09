# DSAQueue
import numpy as np


class DSAQueue:
    def __init__(self, n=100):
        self.queue = np.empty(n, dtype=object)
        self.count = 0

    def get_count(self):
        return self.count

    def is_empty(self):
        empty = False
        if self.count == 0:
            empty = True
        return empty

    def is_full(self):
        full = False
        if self.count == len(self.queue):
            full = True
        return full

    def enqueue(self, value):
        try:
            self.queue[self.count] = value
            self.count += 1
        except:
            print("...\nQueue full!")

    def dequeue(self):
        last_val = self.queue[self.count-1]
        del self.queue[self.count-1]
        self.count -= 1
        return last_val

    def peek(self):
        return self.queue[self.count-1]

