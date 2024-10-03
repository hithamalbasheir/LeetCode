class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        arr_sum = sum(nums)
        if (target_rem := arr_sum % p) == 0: return 0
        for num in nums:
            if (arr_sum - num) % p == 0:
                return 1
        
        prefix_sum = 0
        rem_map = {0:-1}
        res = len(nums)

        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            remaining = (prefix_sum - target_rem) % p
            if remaining in rem_map:
                res = min(res, i - rem_map[remaining])
            
            rem_map[prefix_sum] = i
        
        return res if res < len(nums) else -1