class ListNode:
    def __init__(self, in_value):
        self.value = in_value
        self.next = None

    def get_value(self):
        """this will get the value"""
        return self.value

    def set_value(self, in_value):
        self.value = in_value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        empty = (self.head is None)
        return empty

    def insert_first(self, new_value):
        new_node = ListNode(new_value)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

    def insert_last(self, new_value):
        new_node = ListNode(new_value)
        if self.is_empty():
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.get_next():
                curr_node = curr_node.get_next()
            curr_node.set_next(new_node)

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
            curr_node = self.head
            while curr_node.get_next():
                curr_node = curr_node.get_next()
            node_value = curr_node.get_value()
            return node_value

    def remove_first(self):
        if self.is_empty():
            raise ValueError
        else:
            node_value = self.head.get_value()
            self.head = self.head.get_next()
            return node_value

    def remove_last(self):
        if self.is_empty():
            raise ValueError
        elif not self.head.get_next():
            node_value = self.head.get_value()
            self.head = None
        else:
            prev_node = None
            curr_node = self.head
            while curr_node.get_next():
                prev_node = curr_node
                curr_node = curr_node.get_next()
            prev_node.set_next(None)
            node_value = curr_node.get_value()
        return node_value

    def __iter__(self):
        self._curr = self.head
        return self

    def __next__(self):
        curval = None
        if not self._curr:
            raise StopIteration(print("teh end_"))
        else:
            curval = self._curr.value
            self._curr = self._curr.next
        return curval


class DSAGraph:
    """Uses linked list to store the list of nodes"""
    def __init__(self, vertices=DSALinkedList()):
        self.vertices = vertices

    def add_vertex(self, label, value):
        # init DSAGraphVertex object
        new_vert = DSAGraphVertex(label, value)
        # add to vertices linked list
        self.vertices.insert_last(new_vert)

    def add_edge(self, label1, label2):     # TODO ??
        pass

    def has_vertex(self, label):    # FIXME: weird
        has_v = False
        if label in self.vertices:
            has_v = True
        return has_v

    def get_vertex_count(self):
        pass

    def get_edge_count(self):
        pass

    def get_vertex(self, label):
        pass

    def get_adjacent(self, label):
        pass

    def is_adjacent(self, label1, label2):
        pass

    def display_as_list(self):
        vertices_iter = iter(self.vertices)
        val = next(vertices_iter)
        print("Traversing")
        for val in vertices_iter:
            print(val, end=" --> ")

    def display_as_matrix(self):
        pass


class DSAGraphVertex:
    """Linked lists within each node to store the adjacency list"""
    def __init__(self, label, value, links=DSALinkedList(), visited=False):
        self.label = label
        self.value = value
        self.links = links
        self.visited = visited

    def get_label(self):
        return self.label

    def get_value(self):
        return self.value

    def get_adjacent(self):
        return self.links

    def add_edge(self, vertex):
        self.links.insert_first(vertex)

    def set_visited(self):
        pass

    def clear_visited(self):
        pass

    def get_visited(self):
        pass

    def __str__(self):
        return "Label: {0}\t Value: {1}\tLinks: {2}\t Visited: {3}"\
            .format(self.label, self.value, self.links, self.visited)
