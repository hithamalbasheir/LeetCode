class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        #Cross topological sort
        def get_topological_sort(adjList, n):
            indegree = [0] * n
            nexts = defaultdict(list)
            for i, j in adjList:
                j -= 1
                i -= 1
                indegree[j] += 1
                nexts[i].append(j)
            
            q = []
            for i, j in enumerate(indegree):
                if j == 0:
                    q.append(i)
            res = []
            while q:
                record = q.pop(0)
                res.append(record + 1)
                for nxt in nexts[record]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        q.append(nxt)
            return [] if len(res) != n else res
        
        rows_topo = get_topological_sort(rowConditions, k)
        if not rows_topo: return []

        cols_topo = get_topological_sort(colConditions, k)
        if not cols_topo: return []

        res = [[0 for _ in range(k)] for _ in range(k)]
        idx_pair = defaultdict(list)
        for i, j in enumerate(rows_topo):
           idx_pair[j].append(i)
        for i, j in enumerate(cols_topo):
            idx_pair[j].append(i)
        for num in idx_pair:
            i, j = idx_pair[num]
            res[i][j] = num
        
        return res