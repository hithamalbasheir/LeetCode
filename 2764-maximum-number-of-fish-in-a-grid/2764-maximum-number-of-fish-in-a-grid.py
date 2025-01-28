class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        #Classic DFS from each point + caching
        seen = set()
        rows = len(grid)
        cols = len(grid[0])
        def dfs(i, j):
            in_bound = 0 <= i < rows and 0 <= j < cols
            if (i,j) in seen or not in_bound or not grid[i][j]:
                return 0
            seen.add((i, j))
            return grid[i][j] + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
        res = 0
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i, j))
        return res