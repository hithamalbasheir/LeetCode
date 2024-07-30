class Solution:
    def minimumDeletions(self, s: str) -> int:
        right_side = Counter(list(s))
        left_side = defaultdict(int)
        res = right_side['a']
        for mid in range(len(s)):
            right_side[s[mid]] -= 1
            left_side[s[mid]] += 1
            deletions = left_side['b'] + right_side['a']
            res = min(deletions, res)
        return res