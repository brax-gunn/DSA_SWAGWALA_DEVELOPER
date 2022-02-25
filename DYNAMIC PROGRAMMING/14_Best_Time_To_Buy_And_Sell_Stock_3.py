class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.bestProfit(prices, 0, True, 2, {})
    
    def bestProfit(self, prices, currentIndex, canBuy, transactionsCount, memo):
        if currentIndex >= len(prices) or transactionsCount <= 0:
            return 0
        
        currentKey = (currentIndex,canBuy,transactionsCount)
        if currentKey in memo:
            return memo[currentKey]
        
        idle = self.bestProfit(prices, currentIndex+1, canBuy, transactionsCount, memo)
        if canBuy:
            buy = -prices[currentIndex]  + self.bestProfit(prices, currentIndex+1, False, transactionsCount, memo)
            memo[currentKey] = max(idle, buy)
        else:
            sell = prices[currentIndex] + self.bestProfit(prices, currentIndex+1, True, transactionsCount-1, memo)
            memo[currentKey] = max(idle, sell)
        
        return memo[currentKey]