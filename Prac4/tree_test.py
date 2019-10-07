import treenode as tree
import random

# list of names to be used as values
names = ["Weablo", "Glemdor", "Quamlack", "Tistle", "Marlbornry", "Flantiline",
         "Tennerbro", "Gwizzly", "Howerton", "Norlop", "Streeves", "Bannawack",
         "Terrawom", "Glable", "Glebulp", "Nennafet", "Seeply",
         "Lamaton", "Woorap"]

# list of non repeated keys
#keys = [2,3,4,5,6,8,9,10,12,15,16,166,424,24,42,63,57]

keys = []
for i in range(0, len(names)):
    keys.append(random.randint(0, 1000))


# MANUAL
# adds a node with key: 1 and value: "matt" then displays it
my_node = tree.DSATreeNode(555, "Borideton")
print("Displaying ceremonial MANUAL node: ")
print(my_node)


my_tree = tree.DSABinarySearchTree()
my_tree.insert(777, random.choice(names))

count = 1
for i in range(0, len(names)):
    temp_key = random.choice(keys)
    keys.remove(temp_key)

    temp_name = random.choice(names)
    names.remove(temp_name)

    my_tree.insert(temp_key, temp_name)

    print("\nAt entry number " + str(count) + ", a score of \t" +
          str(temp_key) +
          " was reported for the suburb of \t" + str(temp_name))
    max_node = my_tree.max()
    print("Max: " + str(max_node))
    min_node = my_tree.min()
    print("Min: " + str(min_node))
    count += 1


print("\nFinal tests...")
found = my_tree.find(7)
print(found)

max_node = my_tree.max()
print(max_node)

min_node = my_tree.min()
print(min_node)








