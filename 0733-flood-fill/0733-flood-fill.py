class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        cols = len(image[0])
        rows = len(image)
        def fill(i, j, init_col):
            if not 0 <= i < rows or not 0 <= j < cols:
                return
            if image[i][j] == color or image[i][j] != init_col:
                return
            image[i][j] = color
            fill(i+1, j, init_col)
            fill(i-1, j, init_col)
            fill(i, j+1, init_col)
            fill(i, j-1, init_col)
        fill(sr, sc, image[sr][sc])
        return image