class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        majority = (len(nums)) / 2

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            if hashmap.get(num) >= majority:
                return num

        # for i in hashmap:
        #     if hashmap[i] >= majority:
        #         return i
