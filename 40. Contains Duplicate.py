class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Solved problem using hashset
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

        # Solved problem using hashmap
        hashamp = {}
        for i in nums:
            hashamp[i] = hashamp.get(i, 0) + 1

        for k, v in hashamp.items():
            if v >= 2:
                return True
        return False
