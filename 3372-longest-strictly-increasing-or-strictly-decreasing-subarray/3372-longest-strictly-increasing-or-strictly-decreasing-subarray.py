class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        is_increasing = None
        res = 1
        curr = 1
        for i, num in enumerate(nums[1:], start = 1):
            if nums[i - 1] == num:
                curr = 1
                is_increasing = None
            elif nums[i - 1] > num:
                if is_increasing is True:
                    curr = 2
                    is_increasing = False
                else:
                    curr += 1
            else:
                if is_increasing is True:
                    curr += 1
                else:
                    curr = 2
                is_increasing = True
            res = max(res, curr)
        return res