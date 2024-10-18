class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        
        def dfs(idx, curr):
            if idx == len(nums):
                return 1 if curr == max_or else 0
            
            include = dfs(idx + 1, curr | nums[idx])
            exclude = dfs(idx + 1, curr)
            return include + exclude
        
        return dfs(0, 0)