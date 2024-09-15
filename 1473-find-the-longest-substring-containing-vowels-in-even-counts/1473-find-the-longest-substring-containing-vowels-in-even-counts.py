class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        #No need to check the count of all vowels if it's positive, just xoring the curr value with previous value should be enough
        vowels_map = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

        bitmask = {0: -1}
        curr = 0
        res = 0
        for i, char in enumerate(s):
            if char in vowels_map:
                curr ^= (1 << vowels_map[char])
            
            if curr in bitmask:
                res = max(res, i - bitmask[curr])
            else:
                bitmask[curr] = i
        return res