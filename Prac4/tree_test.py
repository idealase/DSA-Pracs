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

try:
    my_tree.height()
except:
    print("Height check failed")

count = 1
for i in range(0, len(names) // 2):
    temp_key = random.choice(keys)
    keys.remove(temp_key)

    temp_name = random.choice(names)
    names.remove(temp_name)

    my_tree.insert(temp_key, temp_name)

    print("\nAt entry number " + str(count) + ", an ID of \t" +
          str(temp_key) +
          " was reported for the student\t" + str(temp_name))
    max_node = my_tree.max()
    print("\tMax: " + str(max_node))
    min_node = my_tree.min()
    print("\tMin: " + str(min_node))
    count += 1


print("\nFinal tests...")

# find the name of the cheaters!!
found = my_tree.find(777)
print(found)

# find the winner
max_node = my_tree.max()
print(max_node)

# wooden spooner
min_node = my_tree.min()
print(min_node)


print("Generator Display Method")
gen_results = my_tree.generative_print()
print(gen_results)


print("Recursive Display Method")
rec_printed = my_tree.print_tree()
print(rec_printed)




