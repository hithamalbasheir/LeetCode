class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        #Sort the array
        #Do an increasing two pointers going from the minimum upwards and increase the two pointers accordingly till we reach the end of the array
        res = 0
        nums.sort()
        for i, j in enumerate(nums):
            if i == len(nums) - 1:
                return res
            left, right = i, i + 1
            while right < len(nums) and (nums[left] + nums[right]) < target:
                res += 1
                right += 1
        return res