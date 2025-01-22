class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        #Multi source BFS 
        rows, cols = len(isWater), len(isWater[0])
        if rows == 1 and cols == 1: return [[0]]
        res = [[-1 for _ in range(cols)] for _ in range(rows)]
        q = deque([])
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j]:
                    q.append((i, j, -1))
        dirs = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]
        while q:
            i, j, val = q.popleft()
            if res[i][j] != -1 and val != -1:
                continue
            res[i][j] = val + 1
            for x, y in dirs:
                x += i
                y += j
                if 0 <= x < rows and 0 <= y < cols:
                    q.append((x, y, val + 1))
        return res
            