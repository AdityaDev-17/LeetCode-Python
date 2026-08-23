class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        required = [0] * 26

        for char in licensePlate.lower():
            if 'a' <= char <= 'z':
                required[ord(char) - ord('a')] += 1

        answer = ""

        for word in words:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1

            valid = True

            for i in range(26):
                if count[i] < required[i]:
                    valid = False
                    break

            if valid:
                if answer == "" or len(word) < len(answer):
                    answer = word

        return answer