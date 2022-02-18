class Solution:
    def tribonacci(self, n: int) -> int:
        return self.tribProcess(n, {})
    
    def tribProcess(self, n, memo):
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1
        
        currentKey = n
        if currentKey in memo:
            return memo[currentKey]
        
        a = self.tribProcess(n-1, memo)
        b = self.tribProcess(n-2, memo)
        c = self.tribProcess(n-3, memo)
        
        memo[currentKey] = a+b+c
        
        return memo[currentKey]

