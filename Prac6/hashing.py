"""
Practical 8 - Hashing

Implement hash table
Make hash table automatically resize
Save to and reload from file
"""


class DSAHashTable:
    def __init__(self, hash_array=[], count=0):
        self.hash_array = hash_array
        self.count = count
    pass


class DSAHashEntry:
    def __init__(self, in_key="", in_value=None, state=0):
        self.key = in_key
        self.value = in_value
        self.state = state
    pass
