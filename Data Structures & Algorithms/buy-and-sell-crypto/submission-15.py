class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # highest from right to left
        # minus lowest from left to right

        l = 0
        maxP = 0
        minBuyDay = 0

        for r in range(len(prices)):
            
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r # buying later than curr is cheaper
        return maxP