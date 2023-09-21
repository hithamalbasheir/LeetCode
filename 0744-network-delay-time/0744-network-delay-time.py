class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Dijkstra greedy approach
        #Get all paths, return the max of them if all the nodes are filled with values, start with all of them initialised to inf
        adj_list = defaultdict(list)

        for src, dest, w in times:
            adj_list[src].append((w, dest))
        
        visited = set()
        min_heap = [(0, k)]

        while min_heap:
            total_dist, to = heapq.heappop(min_heap)

            visited.add(to)

            if len(visited) == n:
                return total_dist

            for dist, adj in adj_list[to]:
                if adj not in visited:
                    heapq.heappush(min_heap, (dist+total_dist, adj))

        return -1  