""""
SocialSim.py

"""
import sys

usage = "\t---\tWelcome to SocialSim.py\t---\t\n " \
        "\n\n...\n\n\n" \
        "Instructions...\n\n" \
        "select \'-i\' for ..." \
        "\n\t---\tInteractive Test Mode\t---\t\n " \
        "select \'-s\' for ..." \
        "\n\t---\tSimulation Mode\t---\t\n " \
        "\n\ne.g.\n\t" \
        ">> python SocialSim.py -s netfile eventfile p_like p_follow" \


try:
    run_mode = sys.argv[1]
except IndexError:
    print(usage)
    exit()


if run_mode == "-i":
    print("Int")
elif run_mode == "-s":
    print("Sim")
else:
    print("Hmmmmmm")

