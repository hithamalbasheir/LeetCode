class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        memo = Counter(s)
        odd_counts = 0
        for cnt in memo.values():
            odd_counts += cnt & 1
        
        return odd_counts <= k