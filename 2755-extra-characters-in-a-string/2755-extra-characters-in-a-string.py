class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        n = len(s)

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] + 1

            for prefix in range(1, n - i + 1):
                if s[i: i + prefix] in words:
                    dp[i] = min(dp[i], dp[i + prefix])
        
        return dp[0]