class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        i, j = 1, 1
        while j < n:
            if i & x == 0:
                if j & (n - 1):
                    res |= i
                j <<= 1
            i <<= 1
        return res