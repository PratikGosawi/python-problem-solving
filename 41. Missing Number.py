class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        counter = 0
        while counter <= n:
            if counter not in nums:
                return counter
            counter += 1


