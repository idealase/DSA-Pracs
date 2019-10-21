import se_linked
from random import randint

my_list = se_linked.DSALinkedList()

print("Empty Status: " + str(my_list.is_empty()))

my_list.insert_first(29)
my_list.insert_last(40)

print("Empty Status: " + str(my_list.is_empty()))
print("First: {0}\t Last: {1}".format
      (my_list.peek_first(), my_list.peek_last()))

print("\n Inserting at first and last positions...")
my_list.insert_last(42)
my_list.insert_first(28)
print("First: {0}\t Last: {1}".format
      (my_list.peek_first(), my_list.peek_last()))


print("\n Removing first and last...")
my_list.remove_first()
my_list.remove_last()
print("First: {0}\t Last: {1}".format
      (my_list.peek_first(), my_list.peek_last()))



# testing the iterator
ll = se_linked.DSALinkedList()
rand_range = randint(10, 25)
for i in range(15, rand_range):
    new_node = randint(0, 100)
    ll.insert_first(new_node)


# creating list and getting next value
myiter = iter(ll)
value = next(myiter)

print("\nTraversing list...", end="\t\t")
# using a for loop to go through list
for value in ll:
    print(value, end=" --> ")
print("null")