class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            num = bin(i)[2:]
            num = sum(list(map(int, num)))
            res.append(num)
        return res