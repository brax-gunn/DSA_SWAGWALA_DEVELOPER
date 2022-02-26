class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.totalPaths(0, 0, m-1, n-1, {})
    
    def totalPaths(self,currentRow, currentCol, targetRow, targetCol, memo):
        if currentRow > targetRow or currentCol > targetCol:
            return 0
        
        if currentRow==targetRow and currentCol==targetCol:
            return 1
        
        currentKey = str(currentRow) + "_" + str(currentCol)
        if currentKey in memo:
            return memo[currentKey]
        
        moveRight = self.totalPaths(currentRow, currentCol+1, targetRow, targetCol, memo)
        moveDown = self.totalPaths(currentRow+1, currentCol, targetRow, targetCol, memo)
        
        memo[currentKey] = moveRight+moveDown
        return memo[currentKey]