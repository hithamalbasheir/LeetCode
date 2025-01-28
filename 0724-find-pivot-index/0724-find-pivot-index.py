class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #Pre-processing - prefix sum, post fix sum
        res = -1
        prefix = 0
        sum_of_nums = sum(nums)
        for i, num in enumerate(nums):
            postfix = sum_of_nums - prefix - num
            if prefix == postfix:
                return i
            prefix += num
        return res