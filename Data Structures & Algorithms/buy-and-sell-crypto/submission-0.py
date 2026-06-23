class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        for currentPrice in prices:
            lowest = min(lowest, currentPrice)
            profit = max(profit, currentPrice - lowest)

        return profit if profit > 0 else 0
