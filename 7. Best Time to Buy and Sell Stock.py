class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        profit = 0
        min_num = prices[0]

        for i in range(1, len(prices)):
            if min_num > prices[i]:
                min_num = prices[i]
            else:
                profit = abs(min_num - prices[i])
                if profit > max_profit:
                    max_profit = profit
        return max_profit
