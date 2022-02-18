class Solution:

    def climbStairs(self, n: int) -> int:
        return self.process(0, n, 0, {})

        
    def process(self, ci, n, ans, memo):
        if ci == n:
            return ans+1
        if ci > n:
            return ans
        
        currentKey = ci
        if currentKey in memo:
            return memo[currentKey]
    
        oneJump = self.process(ci+1, n, ans, memo)
        twoJump = self.process(ci+2, n, ans, memo)
        ans = oneJump + twoJump
        memo[currentKey]=ans
        return ans