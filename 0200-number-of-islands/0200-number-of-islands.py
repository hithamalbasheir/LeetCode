class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows , cols = len(grid), len(grid[0])
        def dfs(i, j):
            if not 0 <= i < rows or not 0 <= j < cols or (i,j) in visited or grid[i][j] == "0":
                return
            visited.add((i,j))
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i-1, j)

        islands = 0
        for x in range(rows):
            for y in range(cols):
                if (x,y) not in visited and grid[x][y] == "1":
                    dfs(x,y)
                    islands += 1
        
        return islands