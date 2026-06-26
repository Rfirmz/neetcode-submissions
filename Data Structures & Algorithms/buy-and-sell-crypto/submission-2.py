class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        currMin = prices[0]
        optimalSell = 0
        
        l, r = 0, 0

        while r < len(prices):

            if prices[r] < currMin:
                currMin = prices[r]
                l = r
                next
            
            if (prices[r] - currMin) > optimalSell:
                optimalSell = prices[r] - currMin
            
            r += 1
        
        return optimalSell