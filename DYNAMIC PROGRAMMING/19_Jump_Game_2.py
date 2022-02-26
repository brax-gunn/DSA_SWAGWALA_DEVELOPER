class Solution:
    def jump(self, nums: List[int]) -> int:
        return self.minJumps(nums, 0, {})
    
    def minJumps(self, nums, currentIndex, memo):
        if currentIndex >= len(nums)-1:
            return 0
        
        currentKey = currentIndex
        if currentKey in memo:
            return memo[currentKey]
        
        ans = float('inf')
        for i in range(1, nums[currentIndex]+1):
            tempAns = 1 + self.minJumps(nums, currentIndex+i, memo)
            ans = min(tempAns, ans)
        memo[currentKey] = ans
        return memo[currentKey]