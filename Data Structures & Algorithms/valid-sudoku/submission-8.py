class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_count = defaultdict(int)
            col_count = defaultdict(int)
            row_dup = False
            col_dup = False
            for j in range(9):
                if (board[i][j] != "."):
                    row_count[board[i][j]] += 1
                    if (row_count[board[i][j]] > 1):
                        row_dup = True
                        break
                if (board[j][i] != "."):
                    col_count[board[j][i]] += 1
                    if (col_count[board[j][i]] > 1):
                        col_dup = True
                        break
            
            if (row_dup == True or col_dup == True):
                return False
        

        for i in range(3):
            for j in range(3):
                box = []
                dups = defaultdict(int)
                box.extend(board[i * 3][j * 3: j * 3 + 3])
                box.extend(board[i * 3 + 1][j * 3: j * 3 + 3])
                box.extend(board[i * 3 + 2][j * 3: j * 3 + 3])
            
                print(box)
                for val in box:
                    if (val != "."):
                        dups[val] += 1
                        if (dups[val] > 1):
                            return False
                    
        
        return True