class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                
                val = board[i][j]
                for k in range(n):
                    if k != i and val == board[k][j]:
                        return False
                
                for k in range(n):
                    if k != j and val == board[i][k]:
                        return False
                
                b_row, b_col = 3 * (i // 3), 3 * (j // 3)
                for r in range(b_row, b_row + 3):
                    for c in range(b_col, b_col + 3):
                        if (r, c) != (i, j) and board[r][c] == board[i][j]:
                            return False
        
        return True