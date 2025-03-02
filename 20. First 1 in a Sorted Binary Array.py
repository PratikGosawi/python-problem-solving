# {
# Driver Code Starts

# } Driver Code Ends

# User function Template for python3

class Solution:
    def firstIndex(self, arr):
        # Your code goes here
        left = 0
        right = len(arr) - 1

        if arr[left] == 1:
            return 0
        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == 0:
                left = mid + 1
            elif arr[mid] == 1:
                if arr[mid - 1] == 0:
                    return mid
                else:
                    right = mid - 1
        else:
            return -1


# {
# Driver Code Starts.
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.firstIndex(arr))
        print("~")
# } Driver Code Ends