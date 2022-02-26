class Solution:
    def maximumPath(self, N, Matrix):
        memo = {}
        ans = 0
        for col in range(0, N):
            ans = max(ans, self.maxCost(Matrix, N, 0, col, memo))
        return ans
        
    def maxCost(self, matrix, n, currentRow, currentCol, memo):
        if currentRow < 0 or currentRow >= n or currentCol < 0 or currentCol >= n:
            return 0
        
        if currentRow == n-1:
            return matrix[currentRow][currentCol]
            
        currentKey = (currentRow, currentCol)
        if currentKey in memo:
            return memo[currentKey]
        
        moveLeftDiag = matrix[currentRow][currentCol] + self.maxCost(matrix, n, currentRow+1, currentCol-1, memo)
        moveDown = matrix[currentRow][currentCol] + self.maxCost(matrix, n, currentRow+1, currentCol, memo)
        moveRightDiag = matrix[currentRow][currentCol] + self.maxCost(matrix, n, currentRow+1, currentCol+1, memo)
        
        memo[currentKey] = max([moveLeftDiag, moveDown, moveRightDiag])
        return memo[currentKey]