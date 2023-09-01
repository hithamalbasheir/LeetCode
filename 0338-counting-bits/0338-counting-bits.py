class Solution:
    def countBits(self, n: int) -> List[int]:
        #Optimized - kind of recursive - solution
        res = [0]
        for i in range(1, n+1):
            res.append(res[i >> 1] + i%2)
        return res