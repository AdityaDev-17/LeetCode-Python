import random

class RandomizedSet:

    def __init__(self):
        self.values = []
        self.index = {}

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False

        self.index[val] = len(self.values)
        self.values.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False

        index = self.index[val]
        last_value = self.values[-1]

        self.values[index] = last_value
        self.index[last_value] = index

        self.values.pop()
        del self.index[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()