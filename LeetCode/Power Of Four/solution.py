class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 1 or n % 4 == 0:
            return True
        else:
            return False
        