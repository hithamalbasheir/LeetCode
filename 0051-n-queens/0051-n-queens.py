class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col, pos_diag, neg_diag = set(), set(), set()
        
        board = [['.'] * n for i in range(n)]
        res = []

        def backtrack(r):
            if r == n:
                seg = ["".join(row) for row in board]
                res.append(seg)
                return
            
            for c in range(n):
                if c in col or (r+c) in neg_diag or (r-c) in pos_diag:
                    continue
                
                pos_diag.add(r-c)
                neg_diag.add(r+c)
                col.add(c)
                board[r][c] = 'Q'

                backtrack(r+1)

                pos_diag.remove(r-c)
                neg_diag.remove(r+c)
                col.remove(c)
                board[r][c] = '.'
                
        backtrack(0)
        return res


