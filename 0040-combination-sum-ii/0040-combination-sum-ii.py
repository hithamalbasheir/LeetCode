class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        candidates.sort()
        def dfs(i, curr_sum, curr_sum_items):
            if curr_sum == target:
                res.append(curr_sum_items)
                return
            if i >= n or curr_sum > target:
                return
            
            num = candidates[i]
            dfs(i + 1, curr_sum + num, curr_sum_items + [num])

            while i < n - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            
            dfs(i + 1, curr_sum, curr_sum_items)
        
        dfs(0, 0, [])
        
        return list(res)