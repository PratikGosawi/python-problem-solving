class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = 1
        right = x

        mid = (left + right) // 2

        while mid != 0:
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                mid -= 1
            else:
                return mid

