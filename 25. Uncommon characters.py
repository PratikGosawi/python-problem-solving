# User function Template for python3

class Solution:
    # Function to find uncommon characters between two strings.
    def uncommonChars(self, s1, s2):
        result = ''
        for i in s1:
            if (i not in s2) and (i not in result):
                result = result + i
        for j in s2:
            if (j not in s1) and (j not in result):
                result = result + j
        return "".join(sorted(result))

        # code here


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()
        ob = Solution()
        print(ob.uncommonChars(A, B))

        print("~")
# } Driver Code Ends