import csv
import random
from _utils import *

# set starting numbers for net_file
NETWORK_POP = 100
INFLUENCERS = 20
FOLLOWERS = 50
MAX_INF_FOLS = 20
MAX_NORM_FOLS = 5

# for event file
NORM_POSTS = 3
NORM_MIN_NEG = 0
NORM_MAX_NEG = 1

INF_POSTS = 10
INF_MIN_NEG = 0.5
INF_MAX_NEG = 0.8
NEW_RAND_FOLS = 50

# -----------------------------------------------------------------------
# populate the names list
names = []
with open('bin/RandomNames.csv', 'rt') as file:
    reader = csv.reader(file)
    i = 0
    for row in reader:
        if i < NETWORK_POP:
            names.append(row[1])
            i += 1

# populate the influencers list
influencers = []
for i in range(0, INFLUENCERS):
    temp_inf = random.choice(names)
    if temp_inf not in influencers:
        influencers.append(temp_inf)

# populate the followers list
# followers are those more likely to
followers = []
for i in range(0, FOLLOWERS):
    temp_fol = random.choice(names)
    if temp_fol not in followers:
        followers.append(temp_fol)










# ******************************************************************************

network = SocNet()
for name in names:
    network.add_human(name)

network.display_as_list()

for influencer in influencers:
    for i in range(0, random.randint(0, MAX_INF_FOLS)):
        network.add_relationship(str(influencer), str(random.choice(followers)))

for name in names:
    for i in range(0, random.randint(0, MAX_NORM_FOLS)):
        network.add_relationship(str(name), str(random.choice(names)))

for name in names:
    print("\n ----- " + name + " ------\n")
    print("FOLLOWERS:")
    network.show_followers(name)
    print("\nFOLLOWING:")
    network.show_following(name)

for influencer in influencers:
    temp_neg = random.uniform(0,1)
    network.post(influencer, temp_neg)

for name in names:
    print("\n ----- " + name + " ------\n")
    print("FOLLOWERS:")
    network.show_followers(name)
    print("\nFOLLOWING:")
    network.show_following(name)

network.infection_report()

network.statistics()