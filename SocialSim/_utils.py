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
            raise StopIteration(print("_teh end"))
        else:
            curval = self._curr.value
            self._curr = self._curr.next
        return curval

    def display(self):
        iter_ob = iter(self)
        value = next(iter_ob)
        for value in self:
            print(value, end=" --> ")
        print("null")


class SocNet:
    """Uses linked list to store the list of nodes"""
    def __init__(self, humanoids=LinkedList()):
        self.humanoids = humanoids

    def add_human(self, name, value=None):
        # init DSAGraphVertex object
        new_human = Humanoid(name, value)
        # add to humanoids linked list
        self.humanoids.insert_last(new_human)

    def add_relationship(self, name1, name2):   # TODO ??
        h1 = self.get_human(name1)
        h2 = self.get_human(name2)
        h1.links.insert_last(h2)
        h2.links.insert_last(h1)

    def has_humanoid(self, name):    # FIXME: weird
        has_h = False
        humanoids_iter = iter(self.humanoids)
        hum = next(humanoids_iter)
        for hum in humanoids_iter:
            if hum.name == name:
                has_h = True
        return has_h

    def get_vertex_count(self):
        pass

    def get_edge_count(self):
        pass

    def get_human(self, name):
        humanoids_iter = iter(self.humanoids)
        hum = next(humanoids_iter)
        for hum in humanoids_iter:
            if hum.name == name:
                return hum

    def get_adjacent(self, name):
        h = self.get_human(name)
        h.get_adjacent()

    def show_adjacent(self, name):
        h = self.get_human(name)
        hlinks = h.get_adjacent()
        hlinks.display()

    def is_adjacent(self, label1, label2):
        pass

    def display_as_list(self):
        vertices_iter = iter(self.humanoids)
        val = next(vertices_iter)
        print("SocNet Members:")
        for val in vertices_iter:
            print(val, end="\n")

    def display_as_matrix(self):
        pass


class Humanoid:
    """Linked lists within each node to store the adjacency list"""
    def __init__(self, name, value, visited=False):
        self.name = name
        self.value = value
        self.links = LinkedList()
        self.visited = visited

    def get_name(self):
        return self.name

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
        return "Name: {0}\t\t Value: {1}\t Visited: {2}"\
            .format(self.name, self.value, self.visited)