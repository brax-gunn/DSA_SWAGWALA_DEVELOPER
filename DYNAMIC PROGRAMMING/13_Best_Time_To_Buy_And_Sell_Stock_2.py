class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.bestProfit(prices, 0, True, {})
    
    def bestProfit(self, prices, currentIndex, canBuy, memo):
        if currentIndex >= len(prices):
            return 0
        
        currentKey = (currentIndex,canBuy)
        if currentKey in memo:
            return memo[currentKey]
        
        idle = self.bestProfit(prices, currentIndex+1, canBuy, memo)
        if canBuy:
            buy = -prices[currentIndex]  + self.bestProfit(prices, currentIndex, False, memo)
            memo[currentKey] = max(idle, buy)
        else:
            sell = prices[currentIndex] + self.bestProfit(prices, currentIndex+1, True, memo)
            memo[currentKey] = max(idle, sell)
        
        return memo[currentKey]