class RandomizedSet(object):
    def __init__(self):
        self.array = []
        self.val_to_index = {}

    def insert(self, val):
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.array)
        self.array.append(val)
        return True

    def remove(self, val):
        if val not in self.val_to_index:
            return False
        last_element = self.array[-1]
        idx_to_remove = self.val_to_index[val]
        self.array[idx_to_remove] = last_element
        self.val_to_index[last_element] = idx_to_remove
        self.array.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self):
        return random.choice(self.array)
