class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        #Essentially this is a binary lookup table for numbers, we'll store all of them in a 24 length array log(10^7) < 24
        res = 0
        lookup = [0 for _ in range(25)]
        for num in candidates:
            num = bin(num)[2:]
            for i, bit in enumerate(reversed(num)):
                lookup[i] += int(bit)
                res = max(lookup[i], res)
        return res
            