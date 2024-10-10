class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_right = deque([nums[-1]])

        for i, num in enumerate(reversed(nums[:-1])):
            max_right.appendleft(max(num, max_right[0]))
        res = 0
        left = 0
        for right, num in enumerate(nums):
            while nums[left] > max_right[right]:
                left += 1
            res = max(res, right - left)
        return res