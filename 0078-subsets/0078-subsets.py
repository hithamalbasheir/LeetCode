class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        #Doing it like a tree - on each number we're either appending it or not, until we arrive to the unique combination
        def dfs(depth):
            if depth >= len(nums):
                res.append(sub[:])
                return 

            sub.append(nums[depth])
            dfs(depth + 1)
            sub.pop()
            dfs(depth + 1)

        dfs(0)

        return res
        