class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Two pointer greedy approach
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            min_height = height[right] if height[right] < height[left] else height[left]
            curr = min_height * (right - left)
            res = res if res > curr else curr
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return res