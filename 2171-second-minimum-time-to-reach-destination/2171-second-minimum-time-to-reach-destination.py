class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = defaultdict(list)
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)

        q = deque([1])
        cur_time = 0
        res = -1
        visit_times = defaultdict(list)
        while q:
            m = len(q)
            for i in range(m):
                node = q.popleft()
                if node == n:
                    if res != -1: #2nd best time
                        return cur_time
                    res = cur_time
                for nei in adj[node]:
                    nei_times = visit_times[nei]
                    s = len(nei_times)
                    if s == 0 or (s == 1 and nei_times[0] != cur_time):
                        q.append(nei)
                        nei_times.append(cur_time)
                    
            if (cur_time // change) % 2 == 1:
                cur_time += change - (cur_time % change)
            cur_time += time

        return -1