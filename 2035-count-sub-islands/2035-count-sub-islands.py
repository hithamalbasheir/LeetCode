class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        count = 0
        n, m = len(grid1), len(grid1[0])
        seen = set()
        def dfs(i, j):
            if not (0 <= i < n) or not (0 <= j < m) or grid2[i][j] != 1 or (i, j) in seen:
                return True
            seen.add((i, j))
            res = True
            if grid1[i][j] != 1:
                res = False
            
            dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]
            for x, y in dirs:
                res = dfs(x+i, j+y) and res
            
            return res
        
        for i in range(n):
            for j in range(m):
                if (i, j) in seen or grid2[i][j] == 0:
                    continue
                if dfs(i, j):
                    count += 1

        return count