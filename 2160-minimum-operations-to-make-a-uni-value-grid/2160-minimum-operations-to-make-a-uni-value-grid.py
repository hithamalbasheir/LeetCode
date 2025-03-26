class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        rows, cols = len(grid), len(grid[0])
        pivot = grid[0][0] % x
        sorted_grid = SortedList()
        for i in range(rows):
            for j in range(cols):
                if (grid[i][j] % x) != pivot:
                    return -1
                sorted_grid.add(grid[i][j])
        n = len(sorted_grid)
        target = sorted_grid[(n // 2)]
        res = 0
        for num in sorted_grid:
            res += abs(num - target) // x
        return res