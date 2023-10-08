class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #DFS, traverse all over the array and memoize as we go 
        rows, cols = len(matrix), len(matrix[0])
        memo = {}
        res = 1
        def dfs(i, j, prev):
            if not rows > i >= 0 <= j < cols or matrix[i][j] <= prev:
                return 0 #No increase in the path or out of bounds
            if (i,j) in memo:
                return memo[(i,j)]
            curr = 1
            num = matrix[i][j]
            curr = max(
                curr,
                1 + dfs(i + 1, j, num),
                1 + dfs(i - 1, j, num),
                1 + dfs(i, j + 1, num),
                1 + dfs(i, j - 1, num),
                )
            memo[(i,j)] = curr
            return curr

        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i, j, -1))

        return res 
            
        