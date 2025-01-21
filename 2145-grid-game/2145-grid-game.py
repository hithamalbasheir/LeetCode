class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        res = float('inf')
        top_sum = sum(grid[0])
        bottom_sum = 0

        for i in range(len(grid[0])):
            top_sum -= grid[0][i]
            res = min(res, max(top_sum, bottom_sum))
            bottom_sum += grid[1][i]
        
        return res