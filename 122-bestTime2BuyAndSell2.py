class Solution:
    def maxProfit(self,prices):
        left = 0 
        right = 1 
        max_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                max_profit +=  (prices[right] - prices[left])
            left = right
            right += 1
        return max_profit