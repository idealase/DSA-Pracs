import treenode as tree
import random

# list of names to be used as values
names = ["Weablo", "Glemdor", "Quamlack", "Tistle", "Marlbornry", "Flantiline",
         "Tennerbro", "Gwizzly", "Howerton", "Norlop", "Streeves", "Bannawack",
         "Terrawom", "Glable", "Glebulp", "Nennafet", "Seeply",
         "Lamaton", "Woorap"]

# list of non repeated keys
keys = [2,3,4,5,6,8,9,10,12,15,16,166,424,24,42,63,57]

# adds a node with key: 1 and value: "matt" then displays it
my_node = tree.DSATreeNode(1, "matt")
print("Displaying node: ")
print(my_node)
print("\n")


my_tree = tree.DSABinarySearchTree()
my_tree.insert(7, random.choice(names))

for i in range(0, 10):
    temp_key = random.choice(keys)
    keys.remove(temp_key)
    temp_name = random.choice(names)
    names.remove(temp_name)
    my_tree.insert(temp_key, temp_name)


found = my_tree.find(7)
print(found)







