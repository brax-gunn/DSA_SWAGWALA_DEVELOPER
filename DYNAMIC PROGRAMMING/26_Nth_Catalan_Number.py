class Solution:
    #Function to find the nth catalan number.
    def findCatalan(self,n):
        return self.nthCatalan(n, {})
    
    def nthCatalan(self, n, memo):
        if n<=1:
            return 1
            
        currentKey = n
        if currentKey in memo:
            return memo[currentKey]
        
        ways = 0
        for i in range(0,n):
            ways += self.nthCatalan(i, memo) * self.nthCatalan(n-i-1, memo)
            
        memo[currentKey] = ways
        return memo[currentKey]