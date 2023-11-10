class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Two pointers solution
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            curr_size = min(height[left], height[right]) * (right - left)
            res = max(res, curr_size)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return res