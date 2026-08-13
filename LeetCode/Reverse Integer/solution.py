class Solution:
    def reverse(self, x: int) -> int:
        print((x > 2**31 -1))
        num = x
        x = abs(x)
        result = 0
        while x != 0:
            mod_num = x % 10
            result = (result * 10) + mod_num
            if result > 2**31:
                return 0
            x = x // 10
            
        
        if num < 0:
            return 0 - result
        else:
            return result