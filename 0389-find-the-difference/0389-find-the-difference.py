class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        #Hashmaps for both arrays, for faster lookups
        s, t = Counter(s), Counter(t)

        for c in t:
            if c not in s or t[c] > s[c]:
                return c
        return ""
        