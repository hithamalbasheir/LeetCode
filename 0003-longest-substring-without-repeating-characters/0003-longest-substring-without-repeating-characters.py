class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        left, right = 0,1
        curr_window = set(s[left])
        res = len(curr_window)
        while left <= right and right < len(s):
            while right < len(s) and s[right] not in curr_window:
                curr_window.add(s[right])
                right += 1
            res = max(res, len(curr_window))
            curr_window.remove(s[left])
            left += 1
        return res