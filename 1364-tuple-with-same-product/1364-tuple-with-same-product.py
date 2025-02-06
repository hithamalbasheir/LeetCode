class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        res = 0
        memo = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                curr = nums[j] * nums[i]
                memo[curr] += 1
                if memo[curr] >= 2:
                    res += 8 * (memo[curr] - 1)
        return res