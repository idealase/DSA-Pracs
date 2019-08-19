"""
Implement Towers of Hanoi algorithm as a python method
"""

# move n disks from peg src to peg dest


def towers(n, src, dest):

    def move_disk(src, dest):
        print("moving top disk from peg " + str(src) + " to peg " + str(dest))

    if n == 1:
        move_disk(src, dest)
    else:
        temp = 6 - src - dest    # the other (non-target) peg
        towers(n-1, src, temp)
        move_disk(src, dest)
        towers(n-1, temp, dest)


towers(3, 1, 2)
