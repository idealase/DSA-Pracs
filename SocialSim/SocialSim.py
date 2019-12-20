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
import sys                  # for taking command line options
import re                   # for parsing input files
import pickle               # for loading/saving
import os                   # for clearing terminal output
from msvcrt import getch    # for "Press any key to continue"
from time import sleep
from _utils import *

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


def nyi(network=None):
    print("SORRY - NOT YET IMPLEMENTED")
    print("Press any key to return to main menu")
    while getch():
        return interactive_splash(network)

# ----------------------------------------------
# INTERACTIVE FUNCTIONS
# ----------------------------------------------


# Load a previously saved network
def load_network(in_net_name: str):
    try:
        in_net_file = open(in_net_name, 'rb')
        network = pickle.load(in_net_file)
        in_net_file.close()
        print("\nSuccessfully loaded network\n")
        return network, interactive_splash(network)
    except FileNotFoundError:
        print("Unable to load network")
        interactive_splash()
    # interactive_splash()


# Set Probabilities
def set_probs(network):
    return nyi(network)


# Node Operations (find, insert, delete)
def node_ops(network):
    print("\nChoose a Node Operation to perform\n"
          "(I)nsert\n"
          "(D)elete\n"
          "(F)ind\n")
    node_op = input()
    if node_op.upper() == "I":  # insert
        try:
            ins_name = input("\nName of person to be inserted: ")
            network.add_human(str(ins_name))
            print("Added " + ins_name + " to network succesfully")
            sleep(1)
        except NameError:
            print("Operation failed - NameError")
    elif node_op.upper() == "D":    # delete
        pass
    elif node_op.upper() == "F":    # find
        try:
            find_name = input("\nName to find in network: ")
            network.find_disp_hum(str(find_name))

        except NameError:
            print("Operation failed - NameError")
    else:
        print("Invalid Selection")

    opt = input("Perform more (n)ode operations or "
                "enter any key to return to main menu")
    if opt.lower() == "n":
        node_ops(network)
    else:
        interactive_splash(network)




# Edge Operations
def edge_ops(network):
    return nyi(network)


# New Post
def post(network):
    return nyi(network)

# Display Network
def display_net(network):
    network.display_as_list()
    print("\nPress any key to return to main menu")
    while getch():
        return interactive_splash(network)


# Display Statistics
    # events in order of popularity
    # people in order of popularity
    # a person's record - #events, #followers, #following etc
def stats(network):
    return nyi(network)

# Update (timestep)
def update(network):
    return nyi(network)


# Save Network
def save_net(network: object, save_net_name: str):
    #try:
    output = open(save_net_name, 'wb')
    pickle.dump(network, output)
    output.close()
    print("Network saved using Pickle")
    return interactive_splash(network)
    #except:
        #print("Error: Network Saving Failed")


def interactive_splash(network=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Main Menu: Select an option from below\n")
    print("(M)ake new Empty Network\n"
          "(L)oad Network\n"
          "Set P(r)obabilities\n"
          "(N)ode Operations\n"
          "(E)dge Operations\n"
          "New (P)ost\n"
          "(D)isplay Network\n"
          "Display S(t)atistics\n"
          "(U)pdate (run a timestep)\n"
          "(S)ave Network\n"
          "E(x)it\n")

    mm_selection = input()

    # INITIALISE NETWORK
    if mm_selection.lower() == "m":
        network = SocNet()
        print("Created new empty network")
        sleep(1)
        return network, interactive_splash(network)

    # LOAD NETWORK
    elif mm_selection.lower() == "l":
        in_net_name = input("Enter name of network file to load: ")
        load_network(in_net_name)

    # SET PROBABILITIES
    elif mm_selection.lower() == "r":
        set_probs(network)

    # NODE OPERATIONS
    elif mm_selection.lower() == "n":
        node_ops(network)

    # EDGE OPERATIONS
    elif mm_selection.lower() == "e":
        edge_ops(network)

    # NEW POST
    elif mm_selection.lower() == "p":
        post(network)

    # DISPLAY NETWORK
    elif mm_selection.lower() == "d":
        display_net(network)

    # DISPLAY STATS
    elif mm_selection.lower() == "t":
        stats(network)

    # UPDATE
    elif mm_selection.lower() == "u":
        update(network)

    # SAVE NETWORK
    elif mm_selection.lower() == "s":
        save_net_name = input("Save network as: ")
        save_net(network, save_net_name)

    # EXIT
    elif mm_selection.lower() == "x":
        print("\nUnplugging from the social network... good bye")
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
        sleep(2)
        interactive_splash()

    elif run_mode == "-s":

        print("Loading Network File...")
        netfile = sys.argv[2]
        sleep(1)
        print("Loaded: " + str(netfile))

        print("Loading Event File...")
        eventfile = sys.argv[3]
        sleep(1)
        print("Loaded: " + str(eventfile))

        print("Loading Prob Like...")
        p_like = sys.argv[4]
        sleep(1)
        print("Prob Like: " + p_like)

        print("Loading Prob Follow...")
        p_follow = sys.argv[5]
        sleep(1)
        print("Prob Follow: " + p_follow)

        simulation_mode(netfile, eventfile, p_like, p_follow)
    else:
        print(usage)
        exit()
except IndexError:
    print(usage)
    exit()




