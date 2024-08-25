class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        left = 0
        right = 0
        curr_window_length = 0
        zeros_count = 0
        while right < len(nums):
            while right < len(nums) and zeros_count <= k:
                num = nums[right]
                if num == 0:
                    zeros_count += 1
                curr_window_length += 1
                right += 1
                temp = curr_window_length
                if zeros_count > k: temp -= 1 
                res = max(res, temp)
            while left < right and zeros_count > k:
                num = nums[left]
                if nums[left] == 0:
                    zeros_count -= 1
                curr_window_length -= 1
                left += 1
        return res