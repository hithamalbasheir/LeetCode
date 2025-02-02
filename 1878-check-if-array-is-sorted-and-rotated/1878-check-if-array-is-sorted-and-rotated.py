class Solution:
    def check(self, nums: List[int]) -> bool:
        start_idx = 0
        
        for i, num in enumerate(nums[1:], start = 1):
            if nums[i - 1] > num:
                print(num)
                start_idx = i
                break
        
        for i in range(start_idx+1, start_idx + len(nums)):
            i %= len(nums)
            print(nums[i])
            if nums[i] < nums[i - 1]:
                return False
        return True