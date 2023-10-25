class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colorNodes = {}
        
        def bfs(i):
            q = [i]
            colorNodes[i] = 0  # Initialize the first node with color 0

            while q:
                currentNode = q.pop(0)
                currentColor = colorNodes[currentNode]

                for neighbor in graph[currentNode]:
                    if neighbor not in colorNodes:
                        neighborColor = 1 if currentColor == 0 else 0
                        colorNodes[neighbor] = neighborColor
                        q.append(neighbor)
                    else:
                        neighborColor = colorNodes[neighbor]
                        if currentColor == neighborColor:
                            return False
            return True
        
        for i in range(len(graph)):
            if i not in colorNodes:
                if not bfs(i):
                    return False
        return True