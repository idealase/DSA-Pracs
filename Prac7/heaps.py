import numpy as np


class DSAHeap:
    def __init__(self, max_size=100):
        self.max_size = max_size
        self.count = 0
        self.array = []

    def add(self, in_priority, in_value=None):
        new_entry = DSAHeapEntry(in_priority, in_value)
        self.array.append(new_entry)
        self.count += 1
        return self._rec_trick_up(len(self.array)-1)

    def remove(self):
        removing = self.array[0]
        print(removing)
        self.array[0] = self.array[len(self.array)-1]
        self.count -= 1
        return self._rec_trick_down(0, self.count)

    def _rec_trick_up(self, curr_idx):
        parent_idx = (curr_idx - 1) // 2
        if curr_idx > 0:
            if self.array[curr_idx].get_priority() > \
                    self.array[parent_idx].get_priority():
                temp = self.array[parent_idx]
                self.array[parent_idx] = self.array[curr_idx]
                self.array[curr_idx] = temp
                return self._rec_trick_up(parent_idx)

    def _rec_trick_down(self, curr_idx, num_items):
        left_child_idx = (curr_idx * 2) + 1
        right_child_idx = left_child_idx + 1

        if left_child_idx < num_items:
            large_idx = left_child_idx
            if right_child_idx < num_items:
                if self.array[left_child_idx].get_priority() > \
                        self.array[right_child_idx].get_priority():
                    large_idx = right_child_idx
            if self.array[large_idx].get_priority() > \
                    self.array[curr_idx].get_priority():
                temp = self.array[large_idx]
                self.array[large_idx] = self.array[curr_idx]
                self.array[curr_idx] = temp
                return self._rec_trick_up(large_idx, num_items)


class DSAHeapEntry:
    def __init__(self, in_priority, in_value):
        self.priority = in_priority
        self.value = in_value

    def get_priority(self):
        return self.priority

    def set_priority(self, new_pri):
        self.priority = new_pri

    def get_value(self):
        return self.value

    def set_value(self, new_val):
        self.value = new_val

    def __str__(self):
        return str(self.value)
