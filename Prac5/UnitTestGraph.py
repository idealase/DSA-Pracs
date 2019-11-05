from graph import *

numPassed = 0
numTests = 0

# TEST 1
# init an empty graph
print("\nTest 1:", end=" ")
try:
    numTests += 1
    test_graph = DSAGraph()
    print("Initialised empty graph")
    numPassed += 1
except:
    print("Failed")

# TEST 2
# init a standalone test node
print("\nTest 2:", end=" ")
try:
    numTests += 1
    test_node = DSAGraphVertex("A", 10)
    print("Initialised standalone test node")
    print(test_node)
    numPassed += 1
except:
    print("Failed")

# TEST 2.5
print("\nTest 2.5:", end=" ")
try:
    numTests += 1
    test_graph.add_vertex(test_node.label, test_node.value)
    print("Added the test node to graph")
    test_graph.display_as_list()
    numPassed += 1
except:
    print("failed")


# TEST 3
# add a node/vertex to the empty test graph
print("\nTest 3:", end=" ")
try:
    numTests += 1
    test_graph.add_vertex("B", 12)
    print("Added node B 12 to graph")
    test_graph.display_as_list()
    numPassed += 1
except:
    print("Failed")

# TEST 4
# check last vertex in graph vertices linked list
print("\nTest 4:", end=" ")
try:
    numTests += 1
    last_vertex = test_graph.vertices.peek_last()
    print(last_vertex)
    numPassed += 1
except:
    print("Failed")

# TEST 5
# add and check some more
print("\nTest 5:", end=" ")
try:
    numTests += 1
    test_graph.add_vertex("C", 14)
    print("Added node")
    print(test_graph.vertices.peek_last())
    test_graph.add_vertex("D", 16)
    print("Added node")
    print(test_graph.vertices.peek_last())
    numPassed += 1
except:
    print("Failed")

# TEST 6
# display as list
print("\nTest 6:", end=" ")
try:
    numTests += 1
    test_graph.display_as_list()
    numPassed += 1
except:
    print("Failed")


# TEST 7
# has vertex check
print("\nTest 7:", end=" ")
try:
    numTests += 1
    test_graph.has_vertex("B")
    numPassed += 1
except:
    print("Failed")

# TEST 8
# display vertices
try:
    numTests += 1
    test_graph.vertices.display()
    numPassed += 1

except:
    print("Failed")

# Print test summary
print("\nNumber PASSED: ", numPassed, "/", numTests)
print("-> ", numPassed/numTests*100, "%\n")
