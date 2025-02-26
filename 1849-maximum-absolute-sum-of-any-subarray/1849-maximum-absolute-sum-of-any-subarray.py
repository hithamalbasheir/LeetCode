class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        #linear solution with pointers
        min_pre, max_pre = 0, 0
        res, curr = 0, 0
        for num in nums:
            curr += num
            no_min = abs(curr - min_pre)
            no_max = abs(curr - max_pre)
            res = max(res, no_max, no_min)
            min_pre = min(min_pre, curr)
            max_pre = max(max_pre, curr)
        return res