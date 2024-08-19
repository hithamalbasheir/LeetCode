class Solution:
    def minSteps(self, n: int) -> int:
        res = float('inf')
        def dfs(curr_copy, curr_len, steps):
            nonlocal res
            if curr_len > n or steps > res:
                return
            if curr_len == n:
                res = min(res, steps)
                return
            dfs(curr_len, 2 * curr_len, steps + 2)
            dfs(curr_copy, curr_len + curr_copy, steps + 1)
        
        dfs(1, 1, 0)
        return res + 1 if res > 0 else 0