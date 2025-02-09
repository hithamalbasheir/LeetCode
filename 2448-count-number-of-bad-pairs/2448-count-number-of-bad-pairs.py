class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        res = 0
        diff_map = defaultdict(int)

        for idx, num in enumerate(nums):
            diff = idx - num
            res += idx - diff_map[diff]
            diff_map[diff] += 1
        
        return res