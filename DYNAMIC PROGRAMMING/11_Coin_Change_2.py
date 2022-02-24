class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self.countOfWays(coins, amount, 0, {})
    
    def countOfWays(self, coins, amount, currentIndex, memo):
        if currentIndex >= len(coins):
            return 0
        
        if amount == 0:
            return 1
        
        currentKey = str(currentIndex) + "_" + str(amount)
        if currentKey in memo:
            return memo[currentKey]
        
        consider = 0
        if coins[currentIndex] <= amount:
            consider = self.countOfWays(coins, amount-coins[currentIndex], currentIndex, memo)
        
        notConsider = self.countOfWays(coins, amount, currentIndex+1, memo)
        
        memo[currentKey] = consider + notConsider
        return memo[currentKey]