class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        #The intersection of rows and columns since all elements are destinct
        m = len(matrix)
        n = len(matrix[0])
        mins = [float('inf')] * m 
        maxes = [float('-inf')] * n
        for i in range(m):
            for j in range(n):
                curr = matrix[i][j]
                mins[i] = min(curr, mins[i])
                maxes[j] = max(curr, maxes[j])
        mins = set(mins)
        res = []
        for num in maxes:
            if num in mins: res.append(num)
        return res