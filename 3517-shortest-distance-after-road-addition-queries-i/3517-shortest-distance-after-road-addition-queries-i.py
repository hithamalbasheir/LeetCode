class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def bfs(start, end, graph):
            heap = [(0, start)]
            distances = [float('inf')] * n
            distances[start] = 0

            while heap:
                curr_dist, curr_node = heappop(heap)
                if curr_node == end:
                    return curr_dist
                
                if curr_dist > distances[curr_node]:
                    continue
                
                for nbr, w in graph[curr_node]:
                    dist = curr_dist + w
                    if dist < distances[nbr]:
                        distances[nbr] = dist
                        heappush(heap, (dist, nbr))
            return distances[end]
        


        adj_list = {v: [] for v in range(n)}
        for i in range(n - 1):
            adj_list[i].append((i + 1, 1))
        res = []
        for src,dest in queries:
            adj_list[src].append(( dest, 1 ))
            shrt_path = bfs(0, n - 1, adj_list)
            res.append(shrt_path)
        return res