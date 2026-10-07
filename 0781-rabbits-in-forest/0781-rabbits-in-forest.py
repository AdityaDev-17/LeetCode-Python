class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        count = {}
        result = 0

        for answer in answers:
            if answer not in count:
                count[answer] = 0

            if count[answer] == 0:
                result += answer + 1

            count[answer] += 1

            if count[answer] == answer + 1:
                count[answer] = 0

        return result