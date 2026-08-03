class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        num1 = 0
        num2 = 1
        while n >= 2:
            sum = num1 + num2
            num1 = num2
            num2 = sum
            n -= 1
        
        return sum