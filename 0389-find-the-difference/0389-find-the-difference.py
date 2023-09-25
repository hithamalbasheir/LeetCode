class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        #Using XOR to cross out all similar characters by the others, and the remaining character is the imposter!
        res = 0
        for i in range(len(t)):
            res ^= ord(s[i]) if i < len(s) else 0
            res ^= ord(t[i])
        
        return chr(res)
            