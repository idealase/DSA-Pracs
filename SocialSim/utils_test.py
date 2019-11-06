from _utils import *

print("\nTEST 1: Make Graph\n")
# make a survivor camp
survivor_camp = SocNet()

print("\nTEST 2: Populate Graph\n")
# populate it
survivor_camp.add_human("Andy")
survivor_camp.add_human("Bob")
survivor_camp.add_human("Charlie")
survivor_camp.add_human("Derrick")
survivor_camp.add_human("Eric")
survivor_camp.add_human("Frederic")
survivor_camp.add_human("Gerrick")
survivor_camp.add_human("Henrique")

print("\nTEST 3: Display as List\n")
survivor_camp.display_as_list()

print("\nTEST 4: Check for Andy\n")
if survivor_camp.has_humanoid("Andy"):
    print("Andy is here")

print("\nTEST 5: Add Relationships\n")
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


print("\nTEST 6: See Bob's Relationships\n")
survivor_camp.show_adjacent("Bob")

print("\nTEST 7: Check if Bob and Charlie are friends\n")
if survivor_camp.is_adjacent("Bob", "Charlie"):
    print("Bob and Charlie are friends")

print("\nTEST 8: Infect Someone\n")
infectee = survivor_camp.get_human("Andy")
infectee.infect()

print("\nTEST 9: Check Infection Status\n")
survivor_camp.infection_report()

print("\nTEST 10: Check Friend Counts\n")
humanoids_iter = iter(survivor_camp.humanoids)
val = next(humanoids_iter)
for val in humanoids_iter:
    print(val.get_name(), val.get_friend_count())

print("\nTEST 11: Humanoid Count\n")
print(survivor_camp.get_humanoid_count())
