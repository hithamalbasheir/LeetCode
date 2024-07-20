class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        res = [[0 for _ in range(len(colSum))] for _ in range(len(rowSum))]
        col_sum = [0 for _ in range(len(colSum))]
        for i in range(len(rowSum)):
            res[i][0] = rowSum[i]
            col_sum[0] += rowSum[i]
        
        for j in range(len(colSum) - 1):
            if col_sum[j] == colSum[j]:
                break
            i = 0
            while col_sum[j] > colSum[j] :
                diff = col_sum[j] - colSum[j]
                sub = min(diff, res[i][j])
                res[i][j] -= sub
                res[i][j + 1] += sub
                col_sum[j] -= sub
                col_sum[j + 1] += sub
                i += 1
        return res
