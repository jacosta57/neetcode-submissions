class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for sell in prices:
            current_profit = sell - buy
            profit = max(profit, current_profit)

            buy = min(buy, sell)
        return profit