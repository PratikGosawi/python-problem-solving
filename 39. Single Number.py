class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # result = {}
        # for i in nums:
        #     result[i] = result.get(i, 0) + 1

        # for k, v in result.items():
        #     if v == 1:
        #         print(k)
        #         return k

        nums.sort()
        if len(nums) == 1:
            return nums[0]
        for i in range(0, len(nums), 2):
            if i != len(nums) - 1:
                if nums[i] == nums[i + 1]:
                    print("pass")
                    print(len(nums) - 1)
                else:
                    return nums[i]
            else:
                return nums[i]
