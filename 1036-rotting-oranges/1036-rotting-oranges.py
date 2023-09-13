class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #I'll use a BFS here with a queue
        #I'll then go over each orange that's rotten and simultaneously rotten it's neighbors if I end up with 0 fresh oranges return a counter, else -1 
        #Have a set of all fresh oranges loop over and fill it and populate the q too
        fresh = set()
        rows = len(grid)
        cols = len(grid[0])
        q = []
        #populate the oranges sets
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append([i,j])
                elif grid[i][j] == 1:
                    fresh.add((i,j))
        #Get done quick
        if not fresh:
            return 0
        #Start the BFS 
        counter = 0
        def rotten_neighbors(pair):
            directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
            x, y = pair
            neighbors = []
            for d in directions:
                i, j = x+d[0], y+d[1]
                if not 0 <= i < rows or not 0 <= j < cols or (i,j) not in fresh:
                    continue
                fresh.remove((i,j))
                neighbors.append([i,j])
            return neighbors
        while q:
            n = len(q)
            new_rotten = 0
            for _ in range(n):
                orange = q.pop(0)
                new_neighbors = rotten_neighbors(orange)
                new_rotten += len(new_neighbors)
                q += new_neighbors
            if new_rotten > 0:
                counter += 1
        return -1 if len(fresh) > 0 else counter


        