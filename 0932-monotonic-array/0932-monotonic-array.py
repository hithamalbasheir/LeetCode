class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        #Sequential search, with two boolean checkers initially set to false, as I'm going I can't set both of them to True, and as long as one of them is False then it's monotonic in some sort!
        if len(nums) <= 1:
            return True
        #Booleans to check if it's growing or decreasing
        is_inc, is_dec = False, False

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                is_inc = True
            elif nums[i] < nums[i-1]:
                is_dec = True
            
            if is_dec and is_inc:
                return False
        
        return True