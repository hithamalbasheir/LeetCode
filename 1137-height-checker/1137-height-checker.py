class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp = sorted(heights)
        res = 0
        for i, ht in enumerate(heights):
            if temp[i] != ht:
                res += 1
        return res