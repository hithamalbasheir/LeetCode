class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        dists = []
        nums.sort()
        l, r = 0, nums[-1]
        n = len(nums)
        def get_pairs(diff):
            left = 0
            res = 0
            for right in range(n):
                while (nums[right] - nums[left] > diff):
                    left += 1
                res += right - left
                
            return res

        while l < r:
            mid = l + ((r - l) // 2)
            pairs = get_pairs(mid)
            if pairs < k:
                l = mid + 1
            else:
                r = mid
        
        return r