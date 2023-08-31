class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        sub = []
        def backtrack(idx, total):
            if total <= 0:
                if total == 0:
                    res.append(sub[:])
                return

            for i in range(idx, len(candidates)):
                if i != idx and candidates[i] == candidates[i-1]:
                    continue
                sub.append(candidates[i])
                backtrack(i + 1, total - candidates[i])
                sub.pop()
        backtrack(0, target)
        return res