class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        arr.sort()
        result = []
        p1 = 0
        p2 = len(arr)-1
        while p1 <= p2:
            if p1 == p2:
                result.append(arr[p2])
            else:
                result.append(arr[p2])
                result.append(arr[p1])
            p1 += 1
            p2 -= 1
        return result


#{
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends