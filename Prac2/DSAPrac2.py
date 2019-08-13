

# Activity 2 - Implement Stacks and Queues

# DSA Stack
# arrays as data structure

# FIXME: ???
class DSAStack:
    def __init__(self, stack, count, def_cap = 100):
        self.stack = stack
        self.count = count
        self.def_cap = def_cap

    def is_full(self):
        """Checks if stack is full"""
        pass

    def push(self, value):
        """add new item to top of stack"""
        if self.is_full():
            print("Stack full")     # FIXME: handle this correctly
            pass
        else:
            self[count] = value
            self.count += 1
        pass

    def pop(self):
        """take top-most item from stack"""
        pass

    def top(self):
        """look at top-most item, leave it on stack"""
        pass

    def is_empty(self):
        """check if stack is empty"""
        pass


# DSAQueue

class DSAQueue:
    def __init__(self, queue, count, def_cap = 100):
        self.queue = queue
        self.count = count
        self.def_cap = def_cap

    def get_count(self):
        return self.count

    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.count == self.def_cap:
            return True
        else:
            return False

    def enqueue(self, value):
        pass        # TODO: implement

    def dequeue(self):
        last_val = self.queue[-1]
        del self.queue[-1]
        return last_val

    def peek(self):
        return self.queue[-1]

