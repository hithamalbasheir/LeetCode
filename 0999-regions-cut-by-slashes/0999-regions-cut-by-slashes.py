class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        #Computer vision ( ْ -  ْ)
        #Scaling up
        rows, cols = len(grid), len(grid)
        scaled_rows, scaled_cols = rows * 3, cols * 3
        scaled_grid = [[0] * scaled_cols for _ in range(scaled_rows)]
        seen = set()

        for i in range(rows):
            for j in range(cols):
                s_row, s_col = i * 3, j * 3
                if grid[i][j] == '\\':
                    scaled_grid[s_row][s_col] = scaled_grid[s_row+1][s_col+1] = scaled_grid[s_row+2][s_col+2] = 1
                elif grid[i][j] == '/':
                    scaled_grid[s_row][s_col+2] = scaled_grid[s_row+1][s_col+1] = scaled_grid[s_row+2][s_col] = 1
        
        def dfs(r, c):
            out_of_bounds = r < 0 or r >= scaled_rows or c < 0 or c >= scaled_cols
            if out_of_bounds or (scaled_grid[r][c] == 1) or (r, c) in seen:
                if not out_of_bounds: seen.add((r, c)) #If it's a one
                return
            seen.add((r, c))
            dirs = [[r, c+1], [r, c - 1], [r + 1, c], [r - 1, c]]
            for i, j in dirs:
                dfs(i, j)

        res = 0
        for i in range(scaled_rows):
            for j in range(scaled_cols):
                if len(seen) == scaled_rows * scaled_cols:
                    return res
                if (i, j) not in seen and scaled_grid[i][j] == 0:
                    dfs(i, j)
                    res += 1
                elif scaled_grid[i][j] == 1:
                    seen.add((i, j))
        return res