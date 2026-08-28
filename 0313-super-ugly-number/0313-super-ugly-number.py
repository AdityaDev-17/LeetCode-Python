class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1] * n

        # One pointer for each prime
        index = [0] * len(primes)

        for i in range(1, n):
            # Find the smallest next possible ugly number
            next_num = min(
                primes[j] * ugly[index[j]]
                for j in range(len(primes))
            )

            ugly[i] = next_num

            # Move every pointer that produced this number
            for j in range(len(primes)):
                if primes[j] * ugly[index[j]] == next_num:
                    index[j] += 1

        return ugly[n - 1]