from graph import *

# init an empty graph
test_graph = DSAGraph()

# init a standalone test node
test_node = DSAGraphVertex("A", 10)
print(test_node)

# add a node/vertex to the empty test graph
test_graph.add_vertex("B", 12)

# check last vertex in graph vertices linked list
last_vertex = test_graph.vertices.peek_last()
print(last_vertex)

test_graph.add_vertex("C", 14)
print(test_graph.vertices.peek_last())

test_graph.add_vertex("D", 16)
print(test_graph.vertices.peek_last())