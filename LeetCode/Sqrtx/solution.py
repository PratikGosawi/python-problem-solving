class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        mid = x // 2

        for i in range(1, x):
            if i*i == x:
                return i
            elif i*i > x:
                return i - 1
        return 1
            

        