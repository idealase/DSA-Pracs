import treenode as tree
import random
import csv

# list of names to be used as values
"""
names = ["Weablo", "Glemdor", "Quamlack", "Tistle", "Marlbornry", "Flantiline",
         "Tennerbro", "Gwizzly", "Howerton", "Norlop", "Streeves", "Bannawack",
         "Terrawom", "Glable", "Glebulp", "Nennafet", "Seeply",
         "Lamaton", "Woorap"]

for i in range(0, len(names)):
    keys.append(random.randint(0, 1000))
"""

verbose = False

names = []
keys = []

with open('RandomNames.csv', 'rt') as file:
    reader = csv.reader(file)
    for row in reader:
        names.append(row[1])
        keys.append(int(row[0]))

# MANUAL
# adds a node with key: 1 and value: "matt" then displays it
my_node = tree.DSATreeNode(13671279, "Brodie Sandford")
print("Displaying ceremonial MANUAL node: ")
print(my_node)


my_tree = tree.DSABinarySearchTree()

try:
    my_tree.height()
except:
    print("Height check failed")

my_tree.insert(my_node.get_key(), my_node.get_value())
my_tree.insert(13485649, "Steve Steverson")

try:
    my_tree.height()
except:
    print("Height check failed")

count = 1
for i in range(0, 100):
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
    my_tree.height()
except:
    print("Height check failed")

# find the name of the cheaters!!
found, max_node, min_node = my_tree.find(13485649), my_tree.max(), my_tree.min()
print(found, max_node, min_node)

# find the winner
max_node = my_tree.max()
winner = my_tree.find(max_node)
print(max_node, winner)

# wooden spooner
min_node = my_tree.min()
loser = my_tree.find(min_node)
print(min_node, loser)


print("Generator Display Method")
gen_results = my_tree.generative_print()
print(gen_results)


print("Recursive Display Method")
rec_printed = my_tree.print_tree()
print(rec_printed)




