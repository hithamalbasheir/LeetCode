class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0,0
        for i in nums:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
        slow = 0
        for i in nums:
            fast = nums[fast]
            slow = nums[slow]
            if slow == fast:
                return fast
        return fast