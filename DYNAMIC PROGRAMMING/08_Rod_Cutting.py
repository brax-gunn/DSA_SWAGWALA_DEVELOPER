class Solution:
    def cutRod(self, price, n):
        return self.maxProfit(price, 0, n, {})
    
    def maxProfit(self, price, currentIndex, n, memo):
        
        if currentIndex >= len(price):
            return 0
            
        currentKey = str(currentIndex) + "_" + str(n)
        if currentKey in memo:
            return memo[currentKey]
            
        consider = 0
        if currentIndex < n:
            consider = price[currentIndex] + self.maxProfit(price, currentIndex, n-(currentIndex+1), memo)
        
        notConsider = self.maxProfit(price, currentIndex+1, n, memo)
        
        memo[currentKey] = max(consider, notConsider)
        return memo[currentKey]