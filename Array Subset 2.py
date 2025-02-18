# Optimized solution

class Solution:
    # Function to check if a is a subset of b.
    def isSubset(self, a, b):
        a.sort()
        b.sort()

        a_length = len(a)
        b_length = len(b)

        i = 0
        j = 0

        if b_length > a_length:
            return False
        else:
            i_contains = False
            while i < b_length:
                i_contains = False
                if b[i] > a[j]:
                    j = j + 1
                else:
                    if b[i] == a[j]:
                        i_contains = True
                    else:
                        break
                    i = i + 1
                    j = j + 1
            return i_contains