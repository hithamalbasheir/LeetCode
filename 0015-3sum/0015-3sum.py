class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left = 1
        right = len(nums) - 1
        sol = []
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if i != 0 and nums[i-1] == nums[i]:
                left += 1
                continue
            base = nums[i]
            a = left 
            b = right
            while a < b:
                x = nums[a]+nums[b]+base
                if (x) == 0:
                    blah = [base,nums[a],nums[b]]
                    if blah not in sol:
                        sol.append([base,nums[a],nums[b]])
                        a += 1
                        while nums[a] == nums[a-1] and a < b:
                            a += 1
                elif (x) > 0:
                    b -= 1
                else:
                    a += 1
            left += 1
        return sol