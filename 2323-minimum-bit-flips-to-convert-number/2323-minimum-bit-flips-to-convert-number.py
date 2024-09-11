class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        if start == goal: return 0
        res = 0
        xor = start ^ goal
        while xor > 0:
            res += xor & 1
            xor >>= 1
        return res