class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m = len(matrix)
        n = len(matrix[0])
        curr_row_start = 0
        curr_row_end = m
        curr_col_start = 0
        curr_col_end = n
        direction = 'r'
        while len(res) < m * n:
            if direction == 'r':
                i = curr_row_start
                for j in range(curr_col_start, curr_col_end):
                    res.append(matrix[i][j])
                if len(res) == m*n: break
                direction = 'd'
                curr_row_start += 1
            if direction == 'd':
                j = curr_col_end - 1
                for i in range(curr_row_start, curr_row_end):
                    res.append(matrix[i][j])
                if len(res) == m*n: break
                direction = 'l'
                curr_col_end -= 1
            if direction == 'l':
                i = curr_row_end - 1
                for j in range(curr_col_end - 1, curr_col_start - 1, -1):
                    res.append(matrix[i][j])
                if len(res) == m*n: break
                direction = 'u'
                curr_row_end -= 1
            if direction == 'u':
                j = curr_col_start
                for i in range(curr_row_end - 1, curr_row_start - 1, -1):
                    res.append(matrix[i][j])
                if len(res) == m*n: break
                direction = 'r'
                curr_col_start += 1
        return res