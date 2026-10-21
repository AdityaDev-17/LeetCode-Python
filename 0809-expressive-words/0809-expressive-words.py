class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:
        result = 0

        for word in words:
            i = 0
            j = 0
            valid = True

            while i < len(s) and j < len(word):
                if s[i] != word[j]:
                    valid = False
                    break

                char = s[i]
                count_s = 0
                count_w = 0

                while i < len(s) and s[i] == char:
                    count_s += 1
                    i += 1

                while j < len(word) and word[j] == char:
                    count_w += 1
                    j += 1

                if count_s < count_w:
                    valid = False
                    break

                if count_s < 3 and count_s != count_w:
                    valid = False
                    break

            if valid and i == len(s) and j == len(word):
                result += 1

        return result