class Solution:
    def arraySum(self, arr):
        counter = 0
        
        def return_sum(counter):
            if counter > len(arr)-1:
                return 0
       
            result = arr[counter] + return_sum(counter+1)
            return result
       
        result = return_sum(counter)
        return result