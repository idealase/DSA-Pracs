from _utils import *

print("\nTEST 1\n")
# make a survivor camp
survivor_camp = SocNet()

print("\nTEST 2\n")
# populate it
survivor_camp.add_human("Andy")
survivor_camp.add_human("Bob")
survivor_camp.add_human("Charlie")
survivor_camp.add_human("Derrick")
survivor_camp.add_human("Eric")
survivor_camp.add_human("Frederic")
survivor_camp.add_human("Gerrick")
survivor_camp.add_human("Henrique")

print("\nTEST 3\n")
survivor_camp.display_as_list()

print("\nTEST 4\n")
if survivor_camp.has_humanoid("Andy"):
    print("Andy is here")

print("\nTEST 5\n")
survivor_camp.add_relationship("Andy", "Bob")
survivor_camp.add_relationship("Andy", "Charlie")
survivor_camp.add_relationship("Andy", "Gerrick")
survivor_camp.add_relationship("Andy", "Derrick")
survivor_camp.add_relationship("Andy", "Eric")
survivor_camp.add_relationship("Charlie", "Bob")
survivor_camp.add_relationship("Eric", "Bob")
survivor_camp.add_relationship("Eric", "Henrique")
survivor_camp.add_relationship("Eric", "Gerrick")
survivor_camp.add_relationship("Derrick", "Bob")
survivor_camp.add_relationship("Derrick", "Henrique")
survivor_camp.add_relationship("Derrick", "Gerrick")


print("\nTEST 6\n")
survivor_camp.show_adjacent("Bob")

print("\nTEST 7\n")
if survivor_camp.is_adjacent("Bob", "Charlie"):
    print("Bob and Charlie are friends")


