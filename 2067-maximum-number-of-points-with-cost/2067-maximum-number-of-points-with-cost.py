class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        #Keep taking optimal choices till we reach the bottom line
        rows, cols = len(points), len(points[0])
        prev_row = points[0]
        for row in points[1:]:
            curr_row = row[:]
            left, right = [0] * cols, [0] * cols
            left[0] = prev_row[0]
            for i in range(1, cols):
                left[i] = max(prev_row[i], left[i - 1] - 1)
            
            right[-1] = prev_row[-1]
            for i in range(cols - 2, -1, -1):
                right[i] = max(right[i + 1] - 1, prev_row[i])
            
            for i, num in enumerate(curr_row):
                curr_row[i] += max(left[i], right[i])
            prev_row = curr_row
        return max(prev_row)