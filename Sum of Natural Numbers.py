class Solution:
    def seriesSum(self, n : int) -> int:
        sum=0
        i=0
        while i <= n:
            sum = sum+i
            i+=1
        return sum