class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        final_count = 0

        for num in nums:
            if num == 1:
                count += 1
                if count > final_count:
                    final_count += 1
            else:
                if final_count > 0:
                    count = 0
        return final_count
