class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for n in grid:
            for m in n:
                if m < 0:
                    count += 1

        return count