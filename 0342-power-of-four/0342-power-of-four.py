class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and math.log2(n) % 2 == 0