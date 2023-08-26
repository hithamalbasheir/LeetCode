class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #Recursive approach
        @cache
        def dfs(s):
            if len(s) == 0:
                return True
            for word in wordDict:
                if s.startswith(word):
                    if dfs(s[len(word):]):
                        return True
            return False
        return dfs(s)
        