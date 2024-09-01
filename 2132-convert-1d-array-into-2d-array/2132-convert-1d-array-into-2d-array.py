class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        res = [[0 for _ in range(n)] for _ in range(m)]
        i, j = 0, 0
        for num in original:
            res[i][j] = num
            j += 1
            if j >= n: 
                i += 1
                j = 0
        return res