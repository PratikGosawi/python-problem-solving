# User function Template for python3
# With following code getting performance issue, its taking more time than expected

class Solution:
    # Function to check if a is a subset of b.
    def isSubset(self, a, b):

        for i in b:
            i_contains = False
            # print(f"i = {i}")
            for j in a:
                if i == j:
                    i_contains = True
                    # print(f"{i} - {j} - {i_contains}")
                    a.remove(j)
                    break
            if i_contains == False:
                return False

        if i_contains == False:
            return False
        else:
            return True

        # Your code here


# {
# Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())

    while (T > 0):
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        ob = Solution()
        if ob.isSubset(a1, a2):
            print("true")
        else:
            print("false")

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends