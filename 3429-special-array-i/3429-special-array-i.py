class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        prev = nums[0]
        for num in nums[1:]:
            if num & 1 == prev & 1:
                return False
            prev = num
        return True