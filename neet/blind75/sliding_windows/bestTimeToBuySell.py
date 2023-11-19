from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        l = 0
        r = 1
        max_profit = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit <= 0:
                l = r
            else:
                max_profit = max(max_profit, profit)
            r += 1
        return max_profit