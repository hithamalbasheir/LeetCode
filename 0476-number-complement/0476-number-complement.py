class Solution:
    def findComplement(self, num: int) -> int:
        res = []
        for bit in bin(num)[2:]:
            res.append(str(abs(int(bit) - 1)))
        return int(''.join(res), 2)