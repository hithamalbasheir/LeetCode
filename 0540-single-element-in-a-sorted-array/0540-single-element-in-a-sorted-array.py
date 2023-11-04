class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #Binary search
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1 #Make it even so then we can check if the single element has shifted our elements or not
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid #It might be at the mid location
        return nums[left]
        