class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm"
        ]

        result = []

        for word in words:
            lower_word = word.lower()

            for row in rows:

                valid = True

                for char in lower_word:
                    if char not in row:
                        valid = False
                        break

                if valid:
                    result.append(word)
                    break

        return result