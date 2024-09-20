class Solution:
    def shortestPalindrome(self, s: str) -> str:
        #Two pointers
        def is_palindrome(s, l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        
        for r in reversed(range(len(s))):
            if is_palindrome(s, 0, r):
                suffix = s[r+1:][::-1]
                return suffix + s
        
        return ""