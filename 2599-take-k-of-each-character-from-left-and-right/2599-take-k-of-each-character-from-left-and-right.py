class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0: return 0
        n = len(s)
        if n < k * 3:
            return -1
        char_occ = {'a': 0, 'b': 0, 'c': 0}
        for char in s:
            char_occ[char] += 1
        if char_occ['a'] < k or char_occ['b'] < k or char_occ['c'] < k:
            return -1 
        
        l, max_window = 0, 0
        for r in range(n):
            char_occ[s[r]] -= 1

            while char_occ['a'] < k or char_occ['b'] < k or char_occ['c'] < k:
                char_occ[s[l]] += 1
                l += 1

            max_window = max(max_window, r - l + 1)
        return n - max_window