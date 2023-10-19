class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = 0
        s, t = list(s), list(t)
        while i < len(s):
            if s[i] == '#':
                s.pop(i)
                if i > 0:
                    s.pop(i-1)
                    i -= 1
            else:
                i += 1
        i = 0
        while i < len(t):
            if t[i] == '#':
                t.pop(i)
                if i > 0:
                    t.pop(i-1)
                    i -= 1
            else:
                i += 1
        return s == t