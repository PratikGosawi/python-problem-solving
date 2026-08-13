class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0

        count = 0
        result = 1

        while n != 0:
            if n % 5 == 0:
                count += 1
                num = n
                while num % 25 == 0:
                    count += 1
                    num = num / 5

            result *= n
            n -= 1
        return count

count 