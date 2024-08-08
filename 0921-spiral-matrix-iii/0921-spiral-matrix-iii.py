class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        step = 0
        while len(res) < rows * cols:
            row_dir, col_dir = dirs[step%4]
            step += 1
            for _ in range((step + 1) // 2):
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    res.append([rStart, cStart])
                rStart += row_dir
                cStart += col_dir
        return res