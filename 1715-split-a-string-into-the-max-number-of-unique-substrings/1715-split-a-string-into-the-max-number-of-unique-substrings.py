class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(idx, memo):
            if idx == len(s):
                return 0
            
            res = 0
            for i in range(idx, len(s)):
                part = s[idx:i+1]
                if part in memo:
                    continue
                memo.add(part)
                res = max(res, 1 + dfs(i + 1, memo))
                memo.remove(part)
            return res
        return dfs(0, set())