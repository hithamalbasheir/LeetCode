class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        """
        It should be at least a 3 * 3 matrix to be able to trap water
                                ===
                                =0=
                                ===
        """
        rows, cols = len(heightMap), len(heightMap[0])
        if rows < 3 or cols < 3:
            return 0
        #ّInitialize a heap and push the items on the borders onto it
        heap = []
        for i in range(len(heightMap)):
            for j in range(len(heightMap[0])):
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1 #Mark it as visited

        level, res = 0, 0
        while heap:
            height, x, y = heapq.heappop(heap)
            level = max(height, level)

            #Going through all 4 position
            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= i < rows and 0 <= j < cols and heightMap[i][j] != -1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))

                    #Checking if it can trap water
                    if heightMap[i][j] < level:
                        res += level - heightMap[i][j]

                    #Mark the cell as visited
                    heightMap[i][j] = -1
        return res          