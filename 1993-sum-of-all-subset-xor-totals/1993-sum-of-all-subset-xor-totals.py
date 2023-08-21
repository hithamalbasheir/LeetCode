class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def dfs(depth, sub):
            nonlocal res
            if depth >= len(nums):
                temp = sub
                res += temp
                return 
            
            dfs(depth+1, sub^nums[depth])
            dfs(depth+1, sub)
        
        dfs(0, 0)

        return res