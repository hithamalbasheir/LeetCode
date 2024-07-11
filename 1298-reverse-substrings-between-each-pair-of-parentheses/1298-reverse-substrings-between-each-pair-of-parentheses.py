class Solution:
    def reverseParentheses(self, s: str) -> str:
        pairs = {}
        pos = []
        for i, j in enumerate(s):
            if j == '(':
                pos.append(i) 
            elif j == ')':
                p = pos.pop()
                pairs[i] = p
                pairs[p] = i
        
        right = True
        i = 0
        res = []

        while i < len(s):
            if s[i] == '(' or s[i] == ')':
                i = pairs[i]
                right = not right
            else:
                res.append(s[i])
            i += 1 if right else -1
        return ''.join(res)