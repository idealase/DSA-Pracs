from _utils import *

# **************************************************************
# Test 1: Initialise an empty graph
# **************************************************************
print("\nTEST 1: Make Graph")
# make a survivor camp
survivor_camp = SocNet()

# **************************************************************
# Test 2: populate it
# **************************************************************
print("\nTEST 2: Populate Graph")
survivor_camp.add_human("Andy")
survivor_camp.add_human("Bob")
survivor_camp.add_human("Charlie")
survivor_camp.add_human("Derrick")
survivor_camp.add_human("Eric")
survivor_camp.add_human("Frederic")
survivor_camp.add_human("Gerrick")
survivor_camp.add_human("Henrique")

# **************************************************************
# Test 3
# **************************************************************
print("\nTEST 3: Display as List")
survivor_camp.display_as_list()

# **************************************************************
# Test 4: Use the has_humanoid() method of SocNet to check if Andy is present
# **************************************************************
print("\nTEST 4: Check for Andy")
if survivor_camp.has_humanoid("Andy"):
    print("Andy is here")

# **************************************************************
# Test 5
# **************************************************************
print("\nTEST 5: Add Relationships")
survivor_camp.add_relationship("Andy", "Bob")
survivor_camp.add_relationship("Andy", "Charlie")
survivor_camp.add_relationship("Andy", "Gerrick")
survivor_camp.add_relationship("Andy", "Derrick")
survivor_camp.add_relationship("Andy", "Eric")
survivor_camp.add_relationship("Derrick", "Andy")
survivor_camp.add_relationship("Derrick", "Eric")
survivor_camp.add_relationship("Derrick", "Frederic")
survivor_camp.add_relationship("Charlie", "Bob")
survivor_camp.add_relationship("Eric", "Bob")
survivor_camp.add_relationship("Eric", "Henrique")
survivor_camp.add_relationship("Eric", "Gerrick")
survivor_camp.add_relationship("Derrick", "Bob")
survivor_camp.add_relationship("Derrick", "Henrique")
survivor_camp.add_relationship("Derrick", "Gerrick")
survivor_camp.add_relationship("Frederic", "Gerrick")
survivor_camp.add_relationship("Frederic", "Henrique")
survivor_camp.add_relationship("Frederic", "Andy")
survivor_camp.add_relationship("Henrique", "Bob")
survivor_camp.add_relationship("Henrique", "Andy")

# **************************************************************
# Test 6
# **************************************************************
print("\nTEST 6: See ALL Bob's Relationships")
survivor_camp.show_adjacent("Bob")
# Test 6.5
print("\nTEST 6.5: See ALL Andy's Relationships")
survivor_camp.show_adjacent("Andy")
# Test 6.6
print("\nTEST 6.6: See Andy's Followers")
survivor_camp.show_followers("Andy")
# Test 6.7
print("\nTEST 6.7: See who Andy Follows")
survivor_camp.show_following("Andy")

# **************************************************************
# Test 7
# **************************************************************
print("\nTEST 7: Check if Bob and Charlie are connected")
if survivor_camp.is_adjacent("Bob", "Charlie"):
    print("Bob and Charlie are connected")

# **************************************************************
# Test 8
# **************************************************************
print("\nTEST 8: Infect Someone")
infectee = survivor_camp.get_human("Andy")
infectee.infect()

# **************************************************************
# Test 9
# **************************************************************
print("\nTEST 9: Check Infection Status")
survivor_camp.infection_report()

# **************************************************************
# Tests 10, 10.1, 10.2 and 10.3
# **************************************************************
humanoids_iter = iter(survivor_camp.humanoids)
val = next(humanoids_iter)
# Test 10
print("\nTEST 10: Check Individual Interaction Counts")
for val in humanoids_iter:
    print(val.get_name(), val.get_friend_count())
# Test 10.1
print("\nTEST 10: Check Individual Follower Counts")
for val in humanoids_iter:
    print(val.get_name(), val.get_follower_count())
# Test 10.2
print("\nTEST 10: Check Individual Following Counts")
for val in humanoids_iter:
    print(val.get_name(), val.get_following_count())
# Test 10.3
print("\nTEST 10.3: Check Network Total Interaction Count")
print(survivor_camp.get_connection_count())

# **************************************************************
# Test 11
# **************************************************************
print("\nTEST 11: Humanoid Count")
print(survivor_camp.get_humanoid_count())

# **************************************************************
# Test 12
# **************************************************************
print("\nTEST 12: Conx")
test_conx = SocConx("Bob", "Charlie")
print("Test Connection as returned by the SocConx str method...")
print(test_conx)
print("Test Connection as returned by the SocConx get_label() method...")
print(test_conx.get_label())

# **************************************************************
# Test 13
# **************************************************************
print("\nTEST 13: Display all Connections using SocConx str method")
survivor_camp.connections.display()

# **************************************************************
# Test 14: Saving a network
# **************************************************************
print("\nTEST 14: Saving with Pickle")
import pickle
try:
    output = open('bin/social_network.pkl', 'wb')
    pickle.dump(survivor_camp, output)
    output.close()
    print("Network saved using Pickle")
except:
    print("Error: Network Saving Failed")

# **************************************************************
# Test 15: Opening a saved network
# **************************************************************
print("\nTEST 15: Opening with Pickle")
try:
    pkl_file = open('bin/social_network.pkl', 'rb')
    pickled_camp = pickle.load(pkl_file)
    pkl_file.close()
    print("opened the pickled camp")
except:
    print("no picklin")


# **************************************************************
# Test 16: POST
# **************************************************************
print("\nTEST 16: Make a Post!!!!!!!!!")
pickled_camp.post("Andy", 0.5)
pickled_camp.post("Frederic", 0.6)
pickled_camp.post("Eric", 0.2)
pickled_camp.post("Charlie", 0.8)
pickled_camp.post("Tom", 0.2)
pickled_camp.display_as_list()
