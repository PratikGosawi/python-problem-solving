class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        ans = 0
        original_num = x
        while x != 0:
            mod_val = x % 10
            ans = (ans * 10) + mod_val
            x = x // 10

        if ans == original_num:
            return True
        else:
            return False

        
        