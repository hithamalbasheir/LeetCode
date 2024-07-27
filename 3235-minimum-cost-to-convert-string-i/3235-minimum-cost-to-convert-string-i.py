class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = defaultdict(list)
        n = len(changed)
        for i in range(n):
            v1, v2, c = original[i], changed[i], cost[i]
            adj[v1].append((v2, c))
        
        def bfs(src):
            heap = [(0, src)]
            min_costs = {}

            while heap:
                cost, node = heappop(heap)
                if node in min_costs:
                    continue
                min_costs[node] = cost
                for nei, nei_cost in adj[node]:
                    heappush(heap, (cost + nei_cost, nei))
            return min_costs
        
        min_cost_maps = {node:bfs(node) for node in set(source)}
        res = 0
        for src, dest in zip(source, target):
            if dest not in min_cost_maps[src]:
                return -1
            res += min_cost_maps[src][dest]
        return res