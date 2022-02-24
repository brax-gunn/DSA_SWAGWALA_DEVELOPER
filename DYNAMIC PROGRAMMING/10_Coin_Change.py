class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        answer = self.leastCoinsRequired(coins, 0, amount, {})
        if answer == float('inf'):
            return -1
        else:
            return answer
    
    def leastCoinsRequired(self, coins, currentIndex, amountLeft, memo):
        if currentIndex >= len(coins):
            return float('inf')
        
        if amountLeft == 0:
            return 0
        
        if amountLeft < 0:
            return float('inf')
        
        currentKey = str(currentIndex)+"_"+str(amountLeft)
        if currentKey in memo:
            return memo[currentKey]
        
        consider = float('inf')
        if coins[currentIndex]<=amountLeft:
            consider = 1 + self.leastCoinsRequired(coins, currentIndex, amountLeft-coins[currentIndex], memo)
        notConsider = self.leastCoinsRequired(coins, currentIndex+1, amountLeft, memo)
        
        memo[currentKey] = min(consider, notConsider)
        return memo[currentKey]