class Solution:
    def factorial(self, n: int) -> int:
        # code here
        
        if n == 0:
            return 1
        
        return n * self.factorial(n-1)
        
        # def find_fact(n):
        #     if n == 1:
        #         return 1
                
        #     return n * find_fact(n-1)
        
        # return find_fact(n)