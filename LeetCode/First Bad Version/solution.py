# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        first_occurance = -1
        mid = -1

        while left <= right:
            mid = (left + right) // 2

            if isBadVersion(mid) == True:
                first_occurance = mid
                right = mid - 1
                # while isBadVersion(mid-1) == True:
                #     mid = mid-1
                # return mid
            else:
                # if first_occurance != -1:
                #     return first_occurance
                left = mid + 1
        return first_occurance
