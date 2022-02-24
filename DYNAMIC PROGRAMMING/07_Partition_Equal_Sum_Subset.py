class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False
        else:
            targetSum = sum(nums)//2
            return self.isTargetSumPossible(nums, 0, targetSum, {})
    
    def isTargetSumPossible(self, nums, currentIndex, targetSum, memo):
        if currentIndex >= len(nums):
            return False
        
        if targetSum==0:
            return True
        if targetSum < 0:
            return False
        
        currentKey = str(currentIndex)+"_"+str(targetSum)
        if currentKey in memo:
            return memo[currentKey]
        
        considerElem = 0
        if nums[currentIndex] <= targetSum:
            considerElem = self.isTargetSumPossible(nums, currentIndex+1, targetSum-nums[currentIndex], memo)