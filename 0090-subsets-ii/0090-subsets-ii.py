class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:   
        nums.sort()     
        res = []
        sub = []
        
        def dfs(depth):
            if depth >= len(nums):
                if not res or res and res[-1] != sub[:]:
                    res.append(sub[:])
                return 
            sub.append(nums[depth])
            if not res or res[-1] != sub:
                dfs(depth+1)

            sub.pop()
            if not res or res[-1] != sub:
                dfs(depth+1)

        dfs(0)
        return res