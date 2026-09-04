class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyIdx = 0
        sellIdx = 1

        while sellIdx < len(prices):
            if prices[buyIdx] < prices[sellIdx]:
                profit = prices[sellIdx] - prices[buyIdx]
                maxProfit = max(maxProfit, profit)
            else:
                buyIdx = sellIdx
            sellIdx += 1
        return maxProfit