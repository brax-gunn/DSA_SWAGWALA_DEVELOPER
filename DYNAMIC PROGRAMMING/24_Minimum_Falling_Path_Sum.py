class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        memo = {}
        
        ans = float('inf')
        for col in range(0, n):
            tempAns = self.minSumCalc(matrix, m, n, 0, col, memo)
            ans = min(tempAns, ans)
        return ans
    
    def minSumCalc(self, matrix, m, n, currentRow, currentCol, memo):
        if currentRow < 0 or currentCol < 0 or currentRow >= m or currentCol >= n:
            return float('inf')
        
        if currentRow == m-1:
            return matrix[currentRow][currentCol]
        
        currentKey = str(currentRow) + "_" + str(currentCol)
        if currentKey in memo:
            return memo[currentKey]
        
        moveLeftDiag = matrix[currentRow][currentCol] + self.minSumCalc(matrix, m, n, currentRow+1, currentCol-1, memo)
        moveDown = matrix[currentRow][currentCol] + self.minSumCalc(matrix, m, n, currentRow+1, currentCol, memo)
        moveRightDiag = matrix[currentRow][currentCol] + self.minSumCalc(matrix, m, n, currentRow+1, currentCol+1, memo)
        
        memo[currentKey] = min([moveLeftDiag, moveDown, moveRightDiag])
        return memo[currentKey]