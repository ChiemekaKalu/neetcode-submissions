class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        profit = 0
        for currentPrice in prices:
            lowest = min(lowest, currentPrice)
            profit = max(profit, currentPrice - lowest)

        return profit 
