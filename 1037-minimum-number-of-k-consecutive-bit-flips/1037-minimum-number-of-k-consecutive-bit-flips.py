class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        curr_flips, res = 0, 0
        
        for i, num in enumerate(nums):
            if i >= k and nums[i - k] == 2:
                curr_flips -= 1
            
            if (curr_flips % 2) == num:
                if i + k > len(nums):
                    return -1
                res += 1
                curr_flips += 1
                nums[i] = 2
        return res