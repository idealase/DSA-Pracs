""""
SocialSim.py

"""
import sys

# Usage Guide to be displayed if program launched incorrectly
usage = "\n\t---\tWelcome to SocialSim.py\t---\t\n " \
        "\n...\n" \
        "Instructions...\n\n" \
        "select \'-i\' for ..." \
        "\n\t---\tInteractive Test Mode\t---\t\n " \
        "select \'-s\' for ..." \
        "\n\t---\tSimulation Mode\t---\t\n " \
        "\n\ne.g.\n\t" \
        ">> python SocialSim.py -s netfile eventfile p_like p_follow" \



def interactive_splash():
    print("\nInteractive Test Mode\n")
    print("Main Menu: Select an option from below")
    print("(1)\t Load Network\n"
          "(2)\t Set Probalities\n"
          "(3)\t Node Operations\n"
          "(4)\t Edge Operations\n"
          "(5)\t New Post\n"
          "(6)\t Display Network\n"
          "(7)\t Display Statistics\n"
          "(8)\t Update (run a timestep)\n"
          "(9)\t Save Network\n")
    mm_selection = input()


def simulation_splash():
    print("\nSimulation Mode\n")

# setting the run mode
try:
    run_mode = sys.argv[1]
    if run_mode == "-i":
        interactive_splash()
    elif run_mode == "-s":
        simulation_splash()
    else:
        print(usage)
        exit()
except IndexError:
    print(usage)
    exit()


# Load Network

# Set Probabilities

# Node Operations

# Edge Operations

# New Post

# Display Network

# Display Statistics
# posts in order of popularity
# people in order of popularity
# a person's record - #posts, #followers, #following etc

# Update (timestep)

# Save Network
import pickle
try:
    output = open('social_network.pkl', 'wb')
    pickle.dump(network, output)
    output.close()
    print("Network saved using Pickle")
except:
    print("Error: Network Saving Failed")



