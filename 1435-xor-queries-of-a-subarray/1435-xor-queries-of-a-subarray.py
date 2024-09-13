class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        memo = {}
        for left, right in queries:
            if ((left, right) in memo):
                res.append(memo[(left, right)])
                continue
            xor = 0
            for i in range(left, right + 1):
                xor ^= arr[i]
            memo[(left, right)] = xor
            res.append(xor)
        return res