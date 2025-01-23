class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        #easy one, just count the sum of rows and the sum of columns, and for each server check if the row sum or the column sum is > 1
        rows, cols = len(grid), len(grid[0])
        if rows == 1 and cols == 1:
            return 0
        row_sum, col_sum = [sum(row) for row in grid], [sum(col) for col in zip(*grid)]
        res = 0
        for i in range(rows):
            for j in range(cols):
                if not grid[i][j]:
                    continue
                if row_sum[i] > 1 or col_sum[j] > 1:
                    res += 1
        return res