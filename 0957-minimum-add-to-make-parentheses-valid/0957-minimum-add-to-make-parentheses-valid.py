class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening = 0 
        closing = 0
        stack = 0
        res = 0
        #)))(((
        for symb in s:
            if symb == '(':
                stack += 1
            else:
                if not stack:
                    res += 1
                else:
                    stack -= 1
        return res + stack