class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adjList = [[] for _ in range(n)]
        
        indegree = [0 for _ in range(n)]
        for src, dest in edges:
            adjList[src].append(dest)
            indegree[dest] += 1
        zero_indegrees = [i for i in range(n) if indegree[i] == 0]
        topo_order = []
        while zero_indegrees:
            curr = zero_indegrees.pop(0)
            topo_order.append(curr)

            #path compression
            for nbr in adjList[curr]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    zero_indegrees.append(nbr)
        
        res = [[] for _ in range(n)]
        res_sets = [set() for _ in range(n)]

        for node in topo_order:
            for nbr in adjList[node]:
                res_sets[nbr].add(node)
                res_sets[nbr].update(res_sets[node])
        
        for i in range(n):
            res[i].extend(res_sets[i])
            res[i].sort()
        return res