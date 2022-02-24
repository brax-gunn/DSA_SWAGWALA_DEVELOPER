class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):
        return self.maxProfit(wt, val, n, W, 0, {})
        
    def maxProfit(self, wt, val, n, w, ci, memo):
        if ci>=n:
            return 0
        
        currentKey = str(ci) + "_" + str(w)
        
        if currentKey in memo:
            return memo[currentKey]
            
        consider = 0
        if wt[ci]<=w:
            consider = val[ci] + self.maxProfit(wt, val, n, w-wt[ci], ci+1, memo)
        
        notConsider = self.maxProfit(wt, val, n, w, ci+1, memo)
        
        memo[currentKey] = max(consider, notConsider)
        return memo[currentKey]