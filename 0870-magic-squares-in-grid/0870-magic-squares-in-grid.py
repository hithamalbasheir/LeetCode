class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0

        def isMagic(r, c):
            cols = [0 for _ in range(3)]
            rows = [0 for _ in range(3)]
            diags = [0 for _ in range(2)]
            seen = set()
            for i in range(r, r+3):
                for j in range(c, c+3):
                    if grid[i][j] in seen or not (1 <= grid[i][j] <= 9):
                        return 0
                    seen.add(grid[i][j])
                    if r - i == c - j:
                        diags[0] += grid[i][j]
                    if i + j == r + 3 - 1 + c:
                        diags[1] += grid[i][j]
                    cols[j % 3] += grid[i][j]
                    rows[i % 3] += grid[i][j]
            diags.append(15) #So dumb of me so I don't have to do an extra check down there lol XD

            for i in range(3):
                if not (cols[i] == rows[i] == diags[i] == 15):
                    return 0
            return 1
    
        res = 0
        for r in range(len(grid) - 2):
            for c in range(len(grid[0]) - 2):
                res += isMagic(r, c)
        return res