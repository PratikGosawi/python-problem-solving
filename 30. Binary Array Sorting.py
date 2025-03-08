class Solution:

    def binSort(self, arr):

        idx = 0
        for i in range(len(arr) - 1):
            if arr[i] == 0:
                idx += 1
            else:
                if arr[i + 1] == 0:
                    arr[idx] = 0
                    arr[i + 1] = 1
                    idx += 1


# {
# Driver Code Starts
# Driver code
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    Solution().binSort(arr)  # sort the binary array

    print(*arr)  # print the sorted array
    print("~")

# } Driver Code Ends