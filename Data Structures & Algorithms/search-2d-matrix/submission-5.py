class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lp, rp = 0, len(matrix) * len(matrix[0]) - 1

        if (matrix[0][0] == target or matrix[-1][-1] == target):
            return True

        while (lp < rp - 1):
            mp = (lp + rp) // 2

            row = mp // len(matrix[0])
            col = mp % len(matrix[0])

            if (matrix[row][col] == target):
                return True
            elif (matrix[row][col] < target):
                lp = mp
            else:
                rp = mp

        return False
