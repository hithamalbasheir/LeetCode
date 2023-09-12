class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #visited set
        #loop through all of the array
        #If I find a 1 and it's not visited I do a dfs from the one figuring out all neighboring cells sum
        #I compare the value with curr_max after I finished the traversal
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        def dfs(i, j):
            if not 0 <= i < rows or not 0 <= j < cols or (i,j) in visited or grid[i][j] == 0:
                return 0
            visited.add((i,j))
            return (1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1))

        curr_max = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1 and (x,y) not in visited:
                    curr_max = max(curr_max, dfs(x, y))
        return curr_max