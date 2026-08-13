class Solution:
    def reverse(self, x: int) -> int:
        num = x
        x = abs(x)
        result = 0
        while x != 0:
            mod_num = x % 10
            result = (result * 10) + mod_num
            x = x // 10
            
        
        if result > (2**31 - 1) or result < -(2**31 - 1):
            return 0
        elif num < 0:
            return 0 - result
        else:
            return result