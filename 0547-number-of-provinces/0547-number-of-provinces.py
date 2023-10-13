class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int: 
        #Do a BFS of DFSs, explore all nodes and check if they form a separate graph, then accordingly deal with them    
        if not isConnected:
            return 0

        n = len(isConnected)
        visit = [False]*n

        #Explore the current node with its neighbors
        def dfs(node):
            for neighbor in range(n):
                if isConnected[node][neighbor] == 1 and not visit[neighbor]:
                    visit[neighbor] = True
                    dfs(neighbor)
        
        res = 0
        for i in range(n):
            if not visit[i]:
                res += 1
                visit[i] = True
                dfs(i)

        return res