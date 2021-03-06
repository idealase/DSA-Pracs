import myStack


class DSATreeNode:
    def __init__(self, in_key, in_value):
        self._key = in_key
        self._value = in_value
        self._left = None
        self._right = None

    def get_key(self):
        return self._key

    def get_value(self):
        return self._value

    def get_left(self):
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

    def _insert_rec(self, key, value, curr):        # FIXME: ???
        update_node = curr
        if not curr:  # base case - found
            update_node = DSATreeNode(key, value)
        elif key == curr.get_key():
            raise ValueError("Key {0} Already in tree".format(key))
        elif key <= curr.get_key():
            curr._left = self._insert_rec(key, value, curr.get_left())
        else:
            curr._right = self._insert_rec(key, value, curr.get_right())
        return update_node

    def delete(self, key):
        pass

    def height(self):
        return self._height_rec(self._root)

    def _height_rec(self, curr):
        if not curr:    # base case
            ht_sofar = -1
        else:
            left_ht = self._height_rec(curr.get_left())
            right_ht = self._height_rec(curr.get_right())
            # get highest of left vs right branches
            if left_ht > right_ht:
                ht_sofar = left_ht + 1
            else:
                ht_sofar = right_ht + 1
        return ht_sofar

    def min(self):
        return self._min_rec(self._root)

    def _min_rec(self, curr):
        if curr.get_left():      # not base case
            min_key = self._min_rec(curr.get_left())
        else:
            min_key = curr.get_key()
        return min_key

    def max(self):
        return self._max_rec(self._root)

    def _max_rec(self, curr):
        if curr.get_right():     # not base case
            max_key = self._max_rec(curr.get_right())
        else:
            max_key = curr.get_key()
        return max_key

    def min_iter(self):
        curr = self._root
        while curr.get_left():
            curr = curr.get_left()
        min_key = curr.get_key()
        return min_key

    def max_iter(self):
        curr = self._root
        while curr.get_right():
            curr = curr.get_right()
        max_key = curr.get_key()
        return max_key

    def generative_print(self):
        return self.gen_data(self._root)

    def gen_data(self, curr):
        """Generator to get tree nodes data"""
        stack = myStack.DSAStack()
        node = curr
        while stack or node:
            if node:
                stack.push(node)
                node = node.get_left()
            else:
                node = stack.pop()
                yield node
                node = node.get_right()

    def print_tree(self):
        return self._rec_print_tree(self._root)

    def _rec_print_tree(self, curr):    # depth first
        if curr.get_left():
            self._rec_print_tree(curr.get_left())
        print(curr)
        if curr.get_right():
            self._rec_print_tree(curr.get_right())



# test harness code
if __name__ == "__main__":
    print("Testing node creation")
    my_node = DSATreeNode(1, "one")
    print(my_node)
