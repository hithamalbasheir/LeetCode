class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(2, rowIndex+2):
            temp = [0] + res[::] + [0]
            row = []
            for j in range(i):
                row.append(temp[j]+temp[j+1])
            res = row[::]
        return res

            