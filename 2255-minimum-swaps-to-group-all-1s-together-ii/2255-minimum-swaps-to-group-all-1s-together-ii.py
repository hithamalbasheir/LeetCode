class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones_count = nums.count(1)
        nums *= 2

        curr_window = nums[0:ones_count]
        curr_ones = max_ones = curr_window.count(1)
        for i in range(ones_count, len(nums)):
            if max_ones == ones_count:
                return 0
            curr_num = curr_window.pop(0)
            if curr_num == 1: curr_ones -= 1
            if nums[i] == 1: curr_ones += 1
            curr_window.append(nums[i])
            max_ones = max(max_ones, curr_ones)
        return ones_count - max_ones