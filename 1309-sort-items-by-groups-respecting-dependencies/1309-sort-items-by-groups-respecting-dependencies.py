class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        #Two tier topological sort / Kahn's Algorithm - on both groups and items
        #Two graphs, one for groups and the other for the items
        def get_topo_sort(graph, indegree):
            topo_sort = []
            q = [node for node in range(len(graph)) if indegree[node] == 0]
            while q:
                v = q.pop()
                topo_sort.append(v)
                for neighbor in graph[v]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)
            return topo_sort if len(topo_sort) == len(graph) else []

        #some trick for a no group items
        for u in range(len(group)):
            if group[u] == -1:
                group[u] = m
                m+=1
        
        #initialize some arrays
        it_indeg = [0] * n
        gr_indeg = [0] * m
        it_graph = [[] for _ in range(n)]
        gr_graph = [[] for _ in range(m)]

        #fill graphs of both items and groups
        for u in range(n):
            for v in beforeItems[u]:
                it_graph[v].append(u)
                it_indeg[u] += 1
                if group[u] != group[v]:
                    gr_graph[group[v]].append(group[u])
                    gr_indeg[group[u]] += 1
        
        #get the topological sort for both groups and items
        items_order = get_topo_sort(it_graph, it_indeg)
        groups_order = get_topo_sort(gr_graph, gr_indeg)
        if not items_order or not groups_order: return []

        #find order within each group
        in_group_order = defaultdict(list)
        for v in items_order:
            in_group_order[group[v]].append(v)
        
        #combine all of that together
        res = []
        for group in groups_order:
            res += in_group_order[group]
        return res

        #This is sooo stressful, ahhhh (-_-