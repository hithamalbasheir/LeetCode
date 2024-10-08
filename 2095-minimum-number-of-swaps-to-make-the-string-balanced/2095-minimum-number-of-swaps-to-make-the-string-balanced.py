class Solution:
    def minSwaps(self, s: str) -> int:
        swaps = 0
        closing = 0
        opening = 0
        s = list(s)
        last_occ = len(s) - 1
        for i in range(len(s)):
            if s[i] == '[':
                opening += 1
            else:
                closing += 1
            if closing > opening:
                while s[last_occ] != ']':
                    last_occ -= 1
                s[i], s[last_occ] = s[last_occ], s[i]
                opening += 1
                closing -= 1
                swaps += 1
        return swaps