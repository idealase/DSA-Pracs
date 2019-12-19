""""
# ----------------------------------------------
SocialSim.py
# ----------------------------------------------

The main python program of the Social Network Simulator

Run SocialSim.py in a terminal as per instructions in usage guide
    Sim - python3 SocialSim.py -s <netfile> <eventfile> <p_like> <p_follow>
    Interactive - python3 SocialSim.py -i

For a self-contained version of the simulation function, you can run combo.py
combo.py is simply a combination of:
    the name generator script name_gen.py, and
    the functionality of SocialSim.py simulation function
combo.py was made to circumvent the need to parse text file input with regex
    - implementing text parsing presented a major bottleneck in development
"""
import sys
from _utils import *
import re
import pickle

# Usage Guide to be displayed if program launched incorrectly
usage = "\n\t---\tWelcome to SocialSim.py\t---\t\n " \
        "\nInstructions...\n" \
        "\n\t---\tInteractive Test Mode\t---\t\n" \
        "use option \'-i\'" \
    "\ne.g. >> python3 SocialSim.py -i" \
    "\n\n\n\t---\tSimulation Mode\t---\t\n" \
    "\nuse option \'-s\'" \
    "NB: simulation mode requires 4 additional input args\n" \
    "\t - a network file\n" \
    "\t - an event file\n" \
    "\t - a base probalility of liking a post\n" \
    "\t - a base probability of following a user\n" \
    "\ne.g. >> python3 SocialSim.py -s netfile eventfile p_like p_follow" \



# FIXME: how???
def breakage_prompt(func):
    """Called after errors in interactive mode
    Gives user the option to try again or exit program"""
    print("Try (a)gain or e(x)it?")
    ans = input()
    if ans.lower() == "a":
        return func
    elif ans.lower() == "x":
        print("Unplugging from the social network... good bye")
        exit()

# ----------------------------------------------
# INTERACTIVE FUNCTIONS
# ----------------------------------------------


# Load a previously saved network
def load_network(in_net_name: str):
    try:
        in_net_file = open(in_net_name, 'rb')
        network = pickle.load(in_net_file)
        in_net_file.close()
        print("Successfully loaded network")
        interactive_splash()
    except:
        print("Unable to load network")
        interactive_splash()


# Set Probabilities


# Node Operations (find, insert, delete)
def node_ops():
    print("Choose a Node Operation to perform\n"
          "(I)nsert\n"
          "(D)elete\n"
          "(F)ind\n")
    node_op = input()
    if node_op.upper() == "I":  # insert
        try:
            ins_name = input("Name of person to be inserted")
            network.add_human(str(ins_name))
        except NameError:
            print("No Network Established")
    elif node_op.upper() == "D":    # delete
        pass
    elif node_op.upper() == "F":    # find
        pass
    else:
        print("Invalid Selection")
# Edge Operations

# New Post

# Display Network

# Display Statistics
    # events in order of popularity
# people in order of popularity
# a person's record - #events, #followers, #following etc

# Update (timestep)


# Save Network
def save_net(save_net_name: str):
    try:
        output = open(save_net_name, 'wb')
        pickle.dump(network, output)
        output.close()
        print("Network saved using Pickle")
    except:
        print("Error: Network Saving Failed")


def interactive_splash():
    print("Main Menu: Select an option from below")
    print("(N)\t Make new Empty Network\n"
          "(1)\t Load Network\n"
          "(2)\t Set Probalities\n"
          "(3)\t Node Operations\n"
          "(4)\t Edge Operations\n"
          "(5)\t New Post\n"
          "(6)\t Display Network\n"
          "(7)\t Display Statistics\n"
          "(8)\t Update (run a timestep)\n"
          "(9)\t Save Network\n"
          "(X)\t Exit\n")
    mm_selection = input()

    if mm_selection.upper() == "N":
        network = SocNet()
        print("Created new empty network")
        return interactive_splash()
    elif mm_selection == "1":   # load
        in_net_name = input("Enter name of network file to load: ")
        load_network(in_net_name)
    elif mm_selection == "2":     # set probs
        pass
    elif mm_selection == "3":     # node ops
        node_ops()
    elif mm_selection == "4":     # edge ops
        pass
    elif mm_selection == "5":     # new post
        pass
    elif mm_selection == "6":     # display net
        pass
    elif mm_selection == "7":     # display stats
        pass
    elif mm_selection == "8":     # update
        pass
    elif mm_selection == "9":     # save
        save_net_name = input("Save network as: ")
        save_net(save_net_name)
    elif mm_selection.upper() == "X":
        print("Unplugging from the social network... good bye")
        exit()
    else:
        print("Error")







# ----------------------------------------------
# SIMULATION MODE
# ----------------------------------------------
def simulation_mode(netfile, eventfile, p_like, p_follow):
    print("\nSimulation Mode\n")

    # init a social network
    network = SocNet()

    with open(netfile, 'r') as network_file:
        #net_line = network_file.readlines()
        print(len(network_file))
        #print(net_line)

    #for line in net_data:
        #print(line)
        #interaction = line.split(":")
        #print(interaction)
        #influencer = interaction[0]
        # follower = interaction[1]




    # handle event file

    # handle probability of likes

    # handle probability of follows


""" handle network file

    with open(netfile, 'r') as network_file:
        net_data = network_file.readlines()
        interactions = []
        ppl = []
        for line in net_data:
            if re.search(":", line):
                re.sub(r"\n", "", line)
                interactions.append(line)
            else:
                ppl.append(line)
        print(interactions)
        print(ppl)"""












# ----------------------------------------------
# PARSING RUN OPTIONS
# ----------------------------------------------
try:
    run_mode = sys.argv[1]
    if run_mode == "-i":
        print("\nInteractive Test Mode\n")
        interactive_splash()
    elif run_mode == "-s":
        print("Loading Network File...")
        netfile = sys.argv[2]
        print("Loaded: " + str(netfile))

        print("Loading Event File...")
        eventfile = sys.argv[3]
        print("Loaded: " + str(eventfile))

        print("Loading Prob Like...")
        p_like = sys.argv[4]
        print("Prob Like: " + p_like)

        print("Loading Prob Follow...")
        p_follow = sys.argv[5]
        print("Prob Follow: " + p_follow)

        simulation_mode(netfile, eventfile, p_like, p_follow)
    else:
        print(usage)
        exit()
except IndexError:
    print(usage)
    exit()




