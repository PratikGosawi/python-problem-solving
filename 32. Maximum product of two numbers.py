#{
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
class Solution:

	def maxProduct(self,arr):
		arr.sort()
		length = len(arr)
		return arr[length-1] * arr[length-2]


#{
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.maxProduct(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends