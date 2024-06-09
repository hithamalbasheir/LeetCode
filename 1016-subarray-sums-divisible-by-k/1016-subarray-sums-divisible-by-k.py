class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_memo = {0 : 1}
        res = 0
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            curr = prefix_memo.get(remainder, 0)
            res += curr
            prefix_memo[remainder] = curr + 1
        return res