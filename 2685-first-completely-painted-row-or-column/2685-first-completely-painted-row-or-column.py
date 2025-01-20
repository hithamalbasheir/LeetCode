class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        mat_map = {}
        rows, cols = len(mat), len(mat[0])
        for i in range(rows):
            for j in range(cols):
                mat_map[mat[i][j]] = (i, j)
        
        paint_row = defaultdict(int)
        paint_col = defaultdict(int)
        for i, num in enumerate(arr):
            row, col = mat_map[num]
            paint_row[row] += 1
            paint_col[col] += 1
            if paint_row[row] == cols or paint_col[col] == rows:
                return i
        return 0