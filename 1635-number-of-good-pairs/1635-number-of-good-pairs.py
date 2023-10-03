class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #A lazy way to get a counter for all nums
        nums_map = Counter(nums)
        res = 0
        for i in nums_map:
            num = nums_map[i]
            res +=  (num * (num - 1))// 2
        return res