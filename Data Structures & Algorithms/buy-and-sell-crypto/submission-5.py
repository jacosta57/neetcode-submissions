class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        profit = 0

        while sell < len(prices):
            current_profit = prices[sell] - prices[buy]
            profit = max(profit, current_profit)
            
            if prices[sell] < prices[buy]:
                buy = sell
            sell += 1
        return profit