class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #Fairly simple solution
        res = []
        sub = []
        def backtrack(path, total):
            if total >= target or path >= len(candidates):
                if target == total:
                    res.append(sub[:])
                return
            num = candidates[path]
            sub.append(num)
            backtrack(path, total + num)
            sub.pop()
            backtrack(path+1, total)
        
        backtrack(0, 0)

        return res