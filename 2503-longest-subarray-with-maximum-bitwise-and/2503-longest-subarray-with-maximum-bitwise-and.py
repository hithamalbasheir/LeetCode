class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = 0
        curr_sum = 0
        res = 0
        for num in nums:
            if num == max_num:
                curr_sum += 1
                res = max(res, curr_sum)
            elif num > max_num:
                max_num = num
                curr_sum = res = 1
            else:
                curr_sum = 0
        return res