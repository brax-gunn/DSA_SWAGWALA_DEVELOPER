class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        ans = 0
        memo = {}
        
        for row in range(0, m):
            for col in range(0, n):
                if matrix[row][col]=="1":
                    tempAns = self.largestSquareValue(matrix, row, col, m, n, memo)
                    ans = max(tempAns*tempAns, ans)
        return ans
            

    def largestSquareValue(self, matrix, currentRow, currentCol, m, n, memo):
        if currentRow >= m or currentCol >= n or matrix[currentRow][currentCol]=="0":
            return 0
        
        currentKey = str(currentRow) + "_" + str(currentCol)
        if currentKey in memo:
            return memo[currentKey]
        
        down = 1 + self.largestSquareValue(matrix, currentRow+1, currentCol, m, n, memo)
        diagonal = 1 + self.largestSquareValue(matrix, currentRow+1, currentCol+1, m, n, memo)
        right = 1 + self.largestSquareValue(matrix, currentRow, currentCol+1, m, n, memo)
        
        memo[currentKey] = min([down, diagonal, right])
        return memo[currentKey]