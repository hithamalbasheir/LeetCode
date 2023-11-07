class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #For each cell do a DFS from the sides going inwards
        #Essesntially, we can just traverse our way from the sides and check which cells are reachable to the pacific ocean and put that in a set, and would do the same for the cells that are on the atlantic ocean, and I'd end up with the intersection of these atlantic and pacific sets
        #To be able to check if a cell is reachable, I'll just check it in increasing order of the height value
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def traverse(i, j, ocean):
            ocean.add((i, j))
            for x, y in ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)):
                if 0 <= x < rows and 0 <= y < cols and (x, y) not in ocean and heights[i][j] <= heights[x][y]:
                    traverse(x, y, ocean)
        
        for j in range(cols):
            #Going from the first column onwards
            traverse(0, j, pacific)
            #Going from the last column backwards 
            traverse(rows - 1, j, atlantic)
        
        for i in range(rows):
            #Going from the first row onwards
            traverse(i, 0, pacific)
            #Going from the last column backwards
            traverse(i, cols - 1, atlantic)
        
        return list(pacific & atlantic)