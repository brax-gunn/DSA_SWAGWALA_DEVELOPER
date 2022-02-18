class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = self.process(0, len(cost), cost, {})
        b = self.process(1, len(cost), cost, {})
        return min(a,b) 
    
    def process(self, ci, n, cost, memo):
        if ci == n:
            return 0
        if ci > n:
            return 1000
        
        currentKey = ci
        if currentKey in memo:
            return memo[currentKey]
        
        oneJump = cost[currentKey] + self.process(ci+1, n, cost, memo)
        twoJump = cost[currentKey] + self.process(ci+2, n, cost, memo)
        
        memo[currentKey] = min(oneJump, twoJump)
        return memo[currentKey]