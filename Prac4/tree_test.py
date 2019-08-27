from treenode import *
import random

names = ["Weablo", "Glemdor", "Quamlack", "Tistle", "Marlbornry", "Flantiline",
         "Tennerbro", "Gwizzly", "Howerton", "Norlop", "Streeves", "Bannawack",
         "Terrawom", "Glable", "Karenton", "Glebulp", "Nennafet", "Seeply",
         "Lamaton", "Woorap"]

my_node = DSATreeNode(1, "matt")
print(my_node)

my_tree = DSABinarySearchTree()


my_tree.insert(7, random.choice(names))

for i in range(0, 18):
    my_tree.insert(random.randint(1,20), random.choice(names))


my_tree.find(7)







