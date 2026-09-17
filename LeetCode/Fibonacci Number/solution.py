class Solution:
    seen = {0:0, 1:1}
    def fib(self, n: int) -> int:
        global seen
        if n in self.seen:
            return self.seen[n]

        self.seen[n] = self.fib(n-1) + self.fib(n-2)
        return self.seen[n]



        # if n == 0:
        #     return 0
        
        # if n == 1:
        #     return 1

        # return (self.fib(n-1) + self.fib(n-2))
    

        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # num1 = 0
        # num2 = 1
        # while n >= 2:
        #     sum = num1 + num2
        #     num1 = num2
        #     num2 = sum
        #     n -= 1
        
        # return sum