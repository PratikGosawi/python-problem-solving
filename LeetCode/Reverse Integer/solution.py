class Solution:
    def reverse(self, x: int) -> int:
        num = x
        x = abs(x)
        result = 0
        while x != 0:
            mod_num = x % 10
            result = (result * 10) + mod_num
            x = int(x / 10)
            if (x < -2**31) or (x > 2**31 -1):
                x = 0
        
        if num < 0:
            return 0 - result
        else:
            return result