class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        alt = 0
        for n in gain:
            alt += n
            res = max(res, alt)
        return res