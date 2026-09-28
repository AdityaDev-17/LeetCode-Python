import random
import bisect

class Solution:

    def __init__(self, rects: list[list[int]]):
        self.rects = rects
        self.prefix = []

        total = 0

        for x1, y1, x2, y2 in rects:
            points = (x2 - x1 + 1) * (y2 - y1 + 1)

            total += points
            self.prefix.append(total)

        self.total = total

    def pick(self) -> list[int]:
        target = random.randint(1, self.total)

        index = bisect.bisect_left(self.prefix, target)

        x1, y1, x2, y2 = self.rects[index]

        x = random.randint(x1, x2)
        y = random.randint(y1, y2)

        return [x, y]