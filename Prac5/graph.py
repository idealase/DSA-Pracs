from se_linked import *


class DSAGraph:
    """Uses linked list to store the list of nodes"""
    def __init__(self, vertices=DSALinkedList()):
        self.vertices = vertices

    def add_vertex(self, label, value=None):
        # init DSAGraphVertex object
        new_vert = DSAGraphVertex(label, value)
        # add to vertices linked list
        self.vertices.insert_last(new_vert)

    def add_connection(self, label1, label2):     # TODO ??
        vertices_iter = iter(self.vertices)
        val = next(vertices_iter)
        for val in vertices_iter:
            if val.label == label1:
                val.links.insert_last(label2)
                print("Connection established")
            elif val.label == label2:
                val.links.insert_last(label1)
                print("Connection completed")
                break
            # print("Label 1 not found")

    def has_vertex(self, label):    # FIXME: weird
        has_v = False
        vertices_iter = iter(self.vertices)
        val = next(vertices_iter)
        for val in vertices_iter:
            if val.label == label:
                has_v = True
        return has_v

    def get_vertex_count(self):
        pass

    def get_edge_count(self):
        pass

    def get_vertex(self, label):
        vertices_iter = iter(self.vertices)
        val = next(vertices_iter)
        for val in vertices_iter:
            if val.label == label:
                return val

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
    def __init__(self, label, value, visited=False):
        self.label = label
        self.value = value
        self.links = DSALinkedList()
        self.visited = visited

    def get_label(self):
        return self.label

    def get_value(self):
        return self.value

    def get_adjacent(self):
        return self.links

    def add_edge(self, vertex_label):
        self.links.insert_first(vertex_label)

    def set_visited(self):
        pass

    def clear_visited(self):
        pass

    def get_visited(self):
        pass

    def __str__(self):
        return "Label: {0}\t Value: {1}\tLinks: {2}\t Visited: {3}"\
            .format(self.label, self.value, self.links, self.visited)
