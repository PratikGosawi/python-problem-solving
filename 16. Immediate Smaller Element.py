class Solution:

	def immediateSmaller(self, arr):
	    for i in range(len(arr)-1):
	        if arr[i] > arr[i+1]:
	            arr[i] = arr[i+1]
            else:
                arr[i] = -1
        arr[len(arr)-1] = -1