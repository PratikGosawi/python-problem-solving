class Solution:
    def largest(self, arr):
        i=0
        max=0
        mark=0
        length_of_array = len(arr)
        if length_of_array > 1:
            while i < length_of_array:
                if i != length_of_array-1:
                    if arr[mark] > arr[i+1]:
                        max = arr[mark]
                    else:
                        max = arr[i+1]
                        mark = i+1
                else:
                    pass
                i = i+1
                # code here
            return max
        else:
            return arr[i]
