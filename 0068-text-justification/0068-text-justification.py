class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        i = 0
        n = len(words)

        while i < n:
            line_words = []
            letters = 0

            # Pack as many words as possible
            while i < n and letters + len(words[i]) + len(line_words) <= maxWidth:
                line_words.append(words[i])
                letters += len(words[i])
                i += 1

            spaces = maxWidth - letters
            gaps = len(line_words) - 1

            # Last line or single-word line
            if i == n or gaps == 0:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                space_per_gap = spaces // gaps
                extra_spaces = spaces % gaps

                line = ""
                for j in range(gaps):
                    line += line_words[j]
                    line += " " * (space_per_gap + (1 if j < extra_spaces else 0))

                line += line_words[-1]

            result.append(line)

        return result