import de_linked

my_list = de_linked.DSALinkedList()


my_list.insert_first(29)
my_list.insert_last(40)
print("Added 29 first and 40 last")

print("Empty Status: " + str(my_list.is_empty()))
print("First Node:")
print(my_list.peek_first())
print("Last Node:")
print(my_list.peek_last())

print("\n Inserting 28 at first and 42 at last positions...")
my_list.insert_last(42)
my_list.insert_first(28)
print("First Node:")
print(my_list.peek_first())
print("Last Node:")
print(my_list.peek_last())

print("\n Removing first and last...")
my_list.remove_first()
my_list.remove_last()

print("First Node:")
print(my_list.peek_first())
print("Last Node:")
print(my_list.peek_last())
