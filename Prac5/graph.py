from se_linked import *


class DSAGraph:
    """Uses linked list to store the list of nodes"""
    def __init__(self, vertices=DSALinkedList()):
        self.vertices = vertices

    def add_vertex(self, label, value):
        # init DSAGraphVertex object
        new_node = DSAGraphVertex(label, value)
        # add to vertices linked list
        self.vertices.insert_last(new_node)

    def add_edge(self, label1, label2):
        pass

    def has_vertex(self, label):
        pass

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
        pass

    def display_as_matrix(self):
        pass


class DSAGraphVertex:
    """Linked lists within each node to store the adjacency list"""
    def __init__(self, label, value, links=DSALinkedList(), visited=[]):
        self.label = label
        self.value = value
        self.links = links
        self.visited = visited

    def get_label(self):
        return self.label

    def get_value(self):
        return self.value

    def get_adjacent(self):
        pass

    def add_edge(self, vertex):
        pass

    def set_visited(self):
        pass

    def clear_visited(self):
        pass

    def get_visited(self):
        pass

    def __str__(self):
        return "Label: {0}\t Value: {1}\tLinks: {2}\t Visited: {3}"\
            .format(self.label, self.value, self.links, self.visited)
