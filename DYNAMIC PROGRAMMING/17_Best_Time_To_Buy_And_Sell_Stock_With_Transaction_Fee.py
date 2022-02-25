class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        return self.bestProfit(prices, 0, True, {}, fee)
    
    def bestProfit(self, prices, currentIndex, canBuy, memo, fee):
        if currentIndex >= len(prices):
            return 0
        
        currentKey = (currentIndex,canBuy)
        if currentKey in memo:
            return memo[currentKey]
        
        idle = self.bestProfit(prices, currentIndex+1, canBuy, memo, fee)
        if canBuy:
            buy = -prices[currentIndex]  + self.bestProfit(prices, currentIndex+1, False, memo, fee)
            memo[currentKey] = max(idle, buy)
        else:
            sell = -fee + prices[currentIndex] + self.bestProfit(prices, currentIndex+1, True, memo, fee)
            memo[currentKey] = max(idle, sell)
        
        return memo[currentKey]