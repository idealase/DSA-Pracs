import csv
import random

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


# --------------------------------------------------------------------------
# generate the net_file
file = open("net_file.txt", "w")
# write names
for name in names:
    file.write(name)
    file.write("\n")

# write influencer:follower for the popular people
# popular people are assigned a random number of followers from the followers
# group, and 1 follower randomly selected from the entire pop.
# NB: duplicates possible
for influencer in influencers:
    # add random no. of followers from followers list
    for i in range(0, random.randint(0, MAX_INF_FOLS)):
        file.write(influencer + ":" + random.choice(followers))
        file.write("\n")
    # add 1 random follower from all names
    file.write(influencer + ":" + random.choice(names))
    file.write("\n")

# write influencer:follower for the normal people
# all normal people get allocated a random number of followers, randomly
# chosen from the entire population
# NB: duplicates and following self possible
for name in names:
    for i in range(0, random.randint(0, MAX_NORM_FOLS)):
        file.write(name + ":" + random.choice(names))
        file.write("\n")
file.close()

# ---------------------------------------------------------------------------
# generate the event_file

events = []

# posts from all users
for name in names:
    for i in range(0, NORM_POSTS):
        negativity_rating = round(random.uniform(NORM_MIN_NEG, NORM_MAX_NEG), 2)
        new_post = "P:" + name + ":" + str(negativity_rating)
        events.append(new_post)

# posts from influencers
for influencer in influencers:
    for i in range(0, INF_POSTS):
        negativity_rating = round(random.uniform(INF_MIN_NEG, INF_MAX_NEG), 2)
        new_post = "P:" + influencer + ":" + str(negativity_rating)
        events.append(new_post)

# random new follows
for i in range(0, NEW_RAND_FOLS):
    new_follower = random.choice(names)
    new_inf = random.choice(names)
    if new_inf != new_follower:
        new_follow = "F:" + new_inf + ":" + new_follower
        events.append(new_follow)

random.shuffle(events)


# ------------------------
# write to txt file
file = open("event_file.txt", "w")
# write events
for event in events:
    file.write(event)
    file.write("\n")
file.close()
