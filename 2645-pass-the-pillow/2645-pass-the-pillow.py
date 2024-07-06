class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        t = 0
        i = 1
        reverse = False
        while t < time:
            if not reverse and i < n:
                i += 1
            elif reverse and i > 0:
                i -= 1
            if i == 1 or i == n:
                reverse = not reverse
            t += 1
        return i