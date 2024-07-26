class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)
        for src, dest, w in edges:
            adj[src].append((dest, w))
            adj[dest].append((src, w))
        
        def bfs(src):
            heap = [(0, src)]
            seen = set()

            while heap:
                dist, node = heappop(heap)
                if node in seen:
                    continue
                seen.add(node)
                for nei, w in adj[node]:
                    nei_dist = dist + w
                    if nei_dist <= distanceThreshold:
                        heappush(heap, (nei_dist, nei))
            return len(seen) - 1
        
        res, min_cnt = -1, n
        for src in range(n):
            cnt = bfs(src)
            if cnt <= min_cnt:
                res = src
                min_cnt = cnt
        return res