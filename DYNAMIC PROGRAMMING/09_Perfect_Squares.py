import math

class Solution:
    def numSquares(self, n: int) -> int:
        nums = [i for i in range(int(math.sqrt(n))+1, 0, -1)]
        return self.leastNumRequired(nums, 0, n, {})
    
    def leastNumRequired(self, nums, currentIndex, n, memo):
        if currentIndex >= len(nums):
            return float('inf')
        
        if n == 0:
            return 0
        
        if n < 0:
            return float('inf')
        
        currentKey = (currentIndex,n)
        if currentKey in memo:
            return memo[currentKey]
        
        consider = float('inf')
        if nums[currentIndex]**2<=n:
            consider = 1 + self.leastNumRequired(nums, currentIndex, n-nums[currentIndex]**2, memo)
        notConsider = self.leastNumRequired(nums, currentIndex+1, n, memo)
        
        memo[currentKey] = min(consider, notConsider)
        return memo[currentKey]