class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        #Heap, dijkstra shortest path
        adj = defaultdict(list)
        
        for i, path in enumerate(edges):
            src, dest = path
            adj[src].append([dest, succProb[i]])
            adj[dest].append([src, succProb[i]])

        #Starting from best possible probability (which is one), negating all values to make it a max heap
        pq = [(-1, start_node)]

        visited = set()

        while pq:
            prob, path = heapq.heappop(pq)
            visited.add(path)

            if path == end_node:
                return prob * -1
            
            for nei, currProb in adj[path]:
                if nei not in visited:
                    heapq.heappush(pq, (prob * currProb, nei))
        return 0


        

        


        

