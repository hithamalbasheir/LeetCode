class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #recursive
        if numRows == 1:
            return [[1]]
        
        prevTriangle = self.generate(numRows-1)
        lastRow = prevTriangle[-1]
        
        newRow = []
        for i in range(len(lastRow)-1):
            newRow.append(lastRow[i] + lastRow[i+1])
        
        newRow = [1] + newRow + [1]
        return prevTriangle + [newRow]

        