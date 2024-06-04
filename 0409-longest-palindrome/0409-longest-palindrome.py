class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars = {}
        odds, evens, ones = 0, 0, 0
        for char in s:
            chars[char] = chars.get(char, 0) + 1
        has_odd = False
        res = 0
        for value in chars.values():
            if value == 1 and not has_odd:
                res += 1
                has_odd = True
            elif value % 2 == 0:
                res += value
            elif value != 1:
                res += value - 1
                if not has_odd:
                    has_odd = True
                    res += 1
        return res
