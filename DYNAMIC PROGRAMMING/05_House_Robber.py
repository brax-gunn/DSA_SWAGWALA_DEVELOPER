class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        return self.maxMoney(nums, n, 0, {})
    
    def maxMoney(self, nums, n, ci, memo):
        if ci >= n:
            return 0
        
        
        currentKey = ci
        if currentKey in memo:
            return  memo[currentKey]
        
        rob = nums[ci] + self.maxMoney(nums, n, ci+2, memo)
        noRob = self.maxMoney(nums, n, ci+1, memo)
        
        memo[currentKey] = max(rob, noRob)
        
        return memo[currentKey]
        