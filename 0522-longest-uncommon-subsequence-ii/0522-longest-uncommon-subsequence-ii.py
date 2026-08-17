class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(s, t):
            i = 0

            for char in t:
                if i < len(s) and s[i] == char:
                    i += 1

            return i == len(s)

        answer = -1

        for i in range(len(strs)):
            uncommon = True

            for j in range(len(strs)):
                if i != j and is_subsequence(strs[i], strs[j]):
                    uncommon = False
                    break

            if uncommon:
                answer = max(answer, len(strs[i]))

        return answer