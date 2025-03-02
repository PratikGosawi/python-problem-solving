# User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self, arr, k):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if k == arr[mid]:
                return True
            elif k > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return False


# {
# Driver Code Starts
# Initial Template for Python 3

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A = [int(x) for x in input().strip().split()]
        k = int(input())
        ob = Solution()
        print("true" if ob.searchInSorted(A, k) else "false")
        print("~")

# } Driver Code Ends