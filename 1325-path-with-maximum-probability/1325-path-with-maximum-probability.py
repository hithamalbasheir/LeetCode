class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        res = 0.0
        adj = defaultdict(list)
        for i in range(len(edges)):
            src, dest = edges[i]
            adj[src].append((dest, succProb[i]))
            adj[dest].append((src, succProb[i]))
        

        max_heap = [(-1.0, start_node)]
        max_prob = {start_node: 1.0}

        while max_heap:
            prob, node = heappop(max_heap)
            prob = -prob
            if node == end_node:
                return prob
            
            for nbr, nbr_prob in adj[node]:
                new_prob = prob * nbr_prob
                if new_prob > max_prob.get(nbr, 0):
                    heappush(max_heap, (-new_prob, nbr))
                    max_prob[nbr] = new_prob
        return 0.0