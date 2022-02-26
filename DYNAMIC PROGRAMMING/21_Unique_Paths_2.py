class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return self.totalPaths(0, 0, m-1, n-1, obstacleGrid, {})
    
    def totalPaths(self,currentRow, currentCol, targetRow, targetCol, obstacleGrid, memo):
        if currentRow > targetRow or currentCol > targetCol:
            return 0
        
        if obstacleGrid[currentRow][currentCol]==1:
            return 0
        
        if currentRow==targetRow and currentCol==targetCol:
            return 1
        
        
        currentKey = str(currentRow) + "_" + str(currentCol)
        if currentKey in memo:
            return memo[currentKey]
        
        moveRight = self.totalPaths(currentRow, currentCol+1, targetRow, targetCol, obstacleGrid, memo)
        moveDown = self.totalPaths(currentRow+1, currentCol, targetRow, targetCol, obstacleGrid, memo)
        
        memo[currentKey] = moveRight+moveDown
        return memo[currentKey]