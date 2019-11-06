from _utils import *

# make a survivor camp
survivor_camp = SocNet()

# populate it
survivor_camp.add_human("Andy")
survivor_camp.add_human("Bob")
survivor_camp.add_human("Charlie")
survivor_camp.add_human("Derrick")
survivor_camp.add_human("Eric")
survivor_camp.add_human("Frederic")
survivor_camp.add_human("Gerrick")
survivor_camp.add_human("Henrique")

survivor_camp.display_as_list()

if survivor_camp.has_humanoid("Andy"):
    print("Andy is here")

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



survivor_camp.show_adjacent("Bob")


