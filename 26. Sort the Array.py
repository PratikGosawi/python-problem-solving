# User function Template for python3
class Solution:
    def sortArr(self, arr):
        for tracker in arr:
            # Bubble Sort
            for i in range(len(arr) - 1):
                if arr[i] < arr[i + 1]:
                    pass
                else:
                    temp = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = temp

        # Selection Sort

        for i in range(len(arr) - 1):
            max_index = 0
            for j in range(max_index + 1, len(arr)):
                if arr[max_index] > arr[j]:
                    temp = arr[max_index]
                    arr[max_index] = arr[j]
                    arr[j] = temp
                    max_index = j
                else:
                    max_index = j

        # return arr.sort()


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        obj = Solution()
        obj.sortArr(arr)
        for i in arr:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends