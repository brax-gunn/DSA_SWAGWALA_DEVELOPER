class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        return self.minPathSumCalc(grid, 0, 0, m, n, {})
    
    def minPathSumCalc(self, grid, currentRow, currentCol, m, n, memo):
        if currentRow >= m or currentCol >= n:
            return float('inf')
        
        if currentRow == m-1 and currentCol == n-1:
            return grid[currentRow][currentCol]
        
        currentKey = str(currentRow) + "_" + str(currentCol)
        if currentKey in memo:
            return memo[currentKey]
        
        moveRight = grid[currentRow][currentCol] + self.minPathSumCalc(grid, currentRow, currentCol+1, m, n, memo)
        moveDown = grid[currentRow][currentCol] + self.minPathSumCalc(grid, currentRow+1, currentCol, m, n, memo)
        
        memo[currentKey] = min(moveRight, moveDown)
        return memo[currentKey]