class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix) // 2):
            for j in range(len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[len(matrix) - i - 1][j]
                matrix[len(matrix) - i - 1][j] = temp
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if (i >= j):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
        
