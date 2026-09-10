class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy low, sell high
        # buy when the left pointer is (↓)
        # sell when the right pointer is high  (↑)
        # always update maxProfit
        l, r = 0, 1 # left = buy. right = sell

        maxProfit = 0

        while r < len(prices):
            #profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit
