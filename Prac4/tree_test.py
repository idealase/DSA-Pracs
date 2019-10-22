import treenode as tree
import random
import csv

verbose = False

names = []
keys = []

with open('RandomNames.csv', 'rt') as file:
    reader = csv.reader(file)
    for row in reader:
        names.append(row[1])
        keys.append(int(row[0]))

# MANUAL adds a node
my_node = tree.DSATreeNode(13671279, "Brodie Sandford")
print("Displaying ceremonial MANUAL node: ")
print(my_node)


my_tree = tree.DSABinarySearchTree()

try:
    print("\nExpected height: 0")
    print("Reported height: ", my_tree.height())
except:
    print("Height check failed")

# add the manually created node, and a new node for steve steversons
my_tree.insert(my_node.get_key(), my_node.get_value())
my_tree.insert(13485649, "Steve Steverson")

try:
    print("\nExpected height: 2")
    print("Reported height: ", my_tree.height())
except:
    print("Height check failed")


# add some random names and IDs to the tree
count = 1
for i in range(0, 23):
    temp_key = random.choice(keys)
    keys.remove(temp_key)

    temp_name = random.choice(names)
    names.remove(temp_name)

    my_tree.insert(temp_key, temp_name)
    max_node = my_tree.max()
    min_node = my_tree.min()
    if verbose:
        print("\nAt entry number " + str(count) + ", an ID of \t" +
              str(temp_key) +
              " was reported for the student\t" + str(temp_name))
        print("\tMax: " + str(max_node))
        print("\tMin: " + str(min_node))
    count += 1



print("\nFinal tests...")

try:
    print("\nExpected height: ???")
    print("Reported height: ", my_tree.height())
except:
    print("Height check failed")


# find the name of the cheaters!!
found, max_node, min_node = my_tree.find(13485649), my_tree.max(), my_tree.min()
print("\nCheater: ", found)
print("\nTesting recursive max/min methods...")
print("Max score: ", max_node)
print("Min score: ", min_node)

# find the winner
winner = my_tree.find(max_node)
print("Winner: ", max_node, winner)

# wooden spooner
loser = my_tree.find(min_node)
print("Loser: ", min_node, loser)


print("\nTesting iterative max/min methods")
try:
    min_node = my_tree.min_iter()
    print("Min: ", min_node)
    max_node = my_tree.max_iter()
    print("Max: ", max_node)
except:
    "Iterative max/min failed"


print("\nGenerator Display Method")
try:
    gen_results = my_tree.generative_print()
    print(gen_results)
except:
    print("Generative display failed")


print("\nRecursive Display Method")
try:
    rec_printed = my_tree.print_tree()
    print(rec_printed)
except:
    print("Recursive display failed")




