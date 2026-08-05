class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True

        def if_sroot_exists(n):
            left = 1
            right = n
            mid = (left + right) // 2

            while left < right:
                if mid*mid == n:
                    return mid
                elif mid*mid > n:
                    mid -= 1
                else:
                    return False
        
        num = if_sroot_exists(n)
        if if_sroot_exists(n):
            if if_sroot_exists(num):
                return True
            else:
                return False
        else:
            return False