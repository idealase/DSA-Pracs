class DSATreeNode:
    def __init__(self, in_key, in_value):
        self._key = in_key
        self._value = in_value
        self._left = None
        self._right = None

    def get_left(self):     # TODO: confirm this method is necessary
        return self._left

    def set_left(self):
        pass

    def get_right(self):
        return self._right

    def set_right(self):
        pass

    def __str__(self):
        return "Key: " + str(self._key) + " Value: " + str(self._value)


class DSABinarySearchTree:
    def __init__(self):
        self._root = None  # start with empty tree

    def find(self, key):  # wrapper method, calls recursive implementations
        return self._find_rec(key, self._root)

    def _find_rec(self, key, curr):
        value = None
        if not curr:  # base case: not found
            raise ValueError("Key " + str(key) + " not found")
        elif key == curr._key:  # base case: found
            value = curr._value
        elif key < curr._key:  # go left (recursive)
            value = self._find_rec(key, curr._left)
        else:  # go right (recursive)
            value = self._find_rec(key, curr._right)
        return value

    def insert(self, key, value):
        self._root = self._insert_rec(key, value, self._root)

    def _insert_rec(self, key, value, curr):
        update_node = curr
        if not curr:  # base case - found
            update_node = DSATreeNode(key, value)
        elif key == curr._key:
            raise ValueError("Already in tree")
        elif key <= curr._key:
            # FIXME: could the below line not simply be curr._left
            # instead of curr.get_left, which just returns curr._left???
            # apparently so
            curr._left = self._insert_rec(key, value, curr._left)
        return update_node



    def delete(self, key):
        pass

    def display(self):
        pass

    def height(self):
        pass

    def min(self):
        return self._min_rec(self._root)

    def _min_rec(self, curr):
        if curr._left:      # not base case
            min_key = self._min_rec(curr._left)
        else:
            min_key = curr._key
        return min_key

    def max(self):
        return self._max_rec(self._root)

    def _max_rec(self, curr):
        if curr._right:     # not base case
            max_key = self._max_rec(curr._right)
        else:
            max_key = curr._key
        return max_key


# test harness code
if __name__ == "__main__":
    print("Testing node creation")
    my_node = DSATreeNode(1, "one")
    print(my_node)
