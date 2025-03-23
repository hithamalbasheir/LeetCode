class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        #Djikstra
        MOD = 10**9 + 7
        adj = defaultdict(list)
        for src, dest, cost in roads:
            adj[src].append((dest, cost))
            adj[dest].append((src, cost))

        heap = [(0, 0)]
        min_cost = [float('inf')] * n
        path_count = [0] * n #There's one path to start with
        path_count[0] = 1

        while heap:
            cost, node = heappop(heap)

            for nei, nei_cost in adj[node]:
                curr_cost = nei_cost + cost
                if curr_cost < min_cost[nei]:
                    min_cost[nei] = cost + nei_cost
                    path_count[nei] = path_count[node]
                    heappush(heap, (cost + nei_cost, nei))
                elif curr_cost == min_cost[nei]:
                    path_count[nei] = path_count[nei] + path_count[node]
                    path_count[nei] %= MOD
        return path_count[n - 1]
