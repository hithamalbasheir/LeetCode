class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        MOD = (1000000000) + 7
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                heappush(sums, curr_sum)
        
        res = 0
        print(sums)
        for _ in range(left - 1):
            heappop(sums)
        
        for _ in range(right - left + 1):
            res += heappop(sums)
        
        return res % MOD
            