class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.isPossible(nums, 0, {})
    
    def isPossible(self, nums, currentIndex, memo):
        if currentIndex >= len(nums)-1:
            return True
        
        currentKey = currentIndex
        if currentKey in memo:
            return memo[currentKey]
        
        ans = False
        for i in range(nums[currentIndex],0,-1):
            tempAns = self.isPossible(nums, currentIndex+i, memo)
            ans = tempAns or ans
        memo[currentKey] = ans
        return memo[currentKey]