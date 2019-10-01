class DSAListNode:
    def __init__(self, in_value):
        self.value = in_value
        self.next = None
        self.prev = None

    def get_value(self):
        """this will get the value"""
        return self.value

    def set_value(self, in_value):
        self.value = in_value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_prev(self):
        return self.prev

    def set_prev(self, new_prev):
        self.prev = new_prev


class DSALinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        empty = (self.head is None)
        return empty

    def insert_first(self, new_value):
        new_node = DSAListNode(new_value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            new_node.set_prev(None)
            self.head = new_node

    def insert_last(self, new_value):
        new_node = DSAListNode(new_value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            curr_node = self.tail
            curr_node.set_next(new_node)
            new_node.set_prev(curr_node)
            self.tail = new_node

    def peek_first(self):
        if self.is_empty():
            raise ValueError
        else:
            node_value = self.head.get_value()
            return node_value

    def peek_last(self):
        if self.is_empty():
            raise ValueError
        else:
            node_value = self.tail.get_value()
            return node_value

    def remove_first(self):
        if self.is_empty():     # empty case
            raise ValueError
        elif not self.head.get_next():      # only one node
            node_value = self.head.get_value()
            self.head = None
            self.tail = None
        else:
            node_value = self.head.get_value()
            self.head = self.head.get_next()
        return node_value

    def remove_last(self):
        if self.is_empty():     # obvious empty case
            raise ValueError
        elif not self.head.get_next():  # single value in list case
            node_value = self.head.get_value()
            self.head = None
            self.tail = None
        else:           # multiple nodes in list
            curr_node = self.tail
            node_value = curr_node.get_value()
            prev_node = curr_node.get_prev()
            prev_node.set_next(None)
            self.tail = prev_node

        return node_value
