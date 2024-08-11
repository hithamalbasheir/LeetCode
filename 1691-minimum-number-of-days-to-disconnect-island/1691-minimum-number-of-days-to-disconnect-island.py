class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        #Check if we have more than one disconnected island
        #Basically we only have 3 solutions, the most minimum that we have to remove is 2 so we can just brute force our way based on that, we first try to run dfs on all of it, if there's more than one island we just return it, and then we try to remove all elements one by one, to test if it can be resolved using one removal, then if both fails we just return 2
        rows, cols = len(grid), len(grid[0])
        def dfs(i, j, seen):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0 or (i, j) in seen:
                return
            seen.add((i, j))
            dirs = [[i, j+1], [i, j-1], [i+1, j], [i-1, j]]
            for r, c in dirs:
                dfs(r, c, seen)

        def get_islands(grid):
            res = 0
            seen = set()
            for i in range(rows):
                for j in range(cols):
                    if (i, j) not in seen and grid[i][j] == 1:
                        dfs(i, j, seen)
                        res += 1
            return res

        #Trying No changes
        if ((num_island := get_islands(grid)) == 0) or num_island > 1:
            return 0

        #Trying to change one element
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    num_islands = get_islands(grid)
                    if num_islands == 0 or num_islands > 1:
                        return 1
                    grid[i][j] = 1
        return 2
