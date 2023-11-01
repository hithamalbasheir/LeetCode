class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0:0, 1:1, 2:1}
        def tri(n):
            if n in memo: return memo[n]
            memo[n] = tri(n -1) + tri(n - 2) + tri(n -3)
            return memo[n]
        return tri(n)