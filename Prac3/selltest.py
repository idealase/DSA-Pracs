import se_linked

my_list = se_linked.DSALinkedList()


my_list.insert_first(29)
my_list.insert_last(40)

print("Empty Status: " + str(my_list.is_empty()))
print(my_list.peek_first())
print(my_list.peek_last())

print("\n Inserting at first and last positions...")
my_list.insert_last(42)
my_list.insert_first(28)
print(my_list.peek_first())
print(my_list.peek_last())

print("\n Removing first and last...")
my_list.remove_first()
my_list.remove_last()
print(my_list.peek_first())
print(my_list.peek_last())
