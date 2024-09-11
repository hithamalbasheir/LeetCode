class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        if start == goal: return 0
        res = 0
        start = bin(start)[2:]
        goal = bin(goal)[2:]
        g = len(goal)
        s = len(start)
        if s > g:
            goal = '0' * (s - g) + goal
        elif g > s:
            start = '0' * (g - s) + start
        for i in range(max(g, s)):
            if start[i] != goal[i]: res += 1
        return res