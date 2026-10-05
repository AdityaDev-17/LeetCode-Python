class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:
        answer = []

        left = 1
        right = k + 1

        while left <= right:
            answer.append(left)
            left += 1

            if left <= right:
                answer.append(right)
                right -= 1

        for num in range(k + 2, n + 1):
            answer.append(num)

        return answer