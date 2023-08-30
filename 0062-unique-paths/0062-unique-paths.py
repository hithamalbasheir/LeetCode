class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #Recursive solution - every m*n grid is essentially the sum of the two grids below it (m, n-1) + (m-1, n)
        memo = {}
        def backtrack(x, y):
            if x == 1 or y == 1:
                return 1
            if ((x-1, y) not in memo):
                memo[(x-1, y)] = backtrack(x-1, y)
            if ((x, y-1) not in memo):
                memo[(x, y-1)] = backtrack(x, y-1)
            return memo[(x-1, y)] + memo[(x, y-1)]
        
        return backtrack(m, n)