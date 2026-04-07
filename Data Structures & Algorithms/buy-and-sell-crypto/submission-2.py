class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_price = 0
        buy = 0
        sell = 1

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                best_price = max(best_price, profit)
            else:
                buy = sell
            sell += 1
        return best_price
        
