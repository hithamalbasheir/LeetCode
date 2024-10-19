class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        n = (1 << n) - 1
        invert_bit = False
        while n > 1:
            mid = n // 2
            if k <= mid:
                n = mid
            elif k > (mid + 1):
                k = 1 + n - k
                n = mid
                invert_bit = not invert_bit
            else:
                return "1" if not invert_bit else "0"
        return "0" if not invert_bit else "1"