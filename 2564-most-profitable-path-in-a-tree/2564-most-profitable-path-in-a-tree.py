class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = defaultdict(list)

        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)

        bobTime = {}
        seen = set()
        res = float('-inf')

        def dfsBob(node, time):
            if node == 0:
                return True

            bobTime[node] = time
            seen.add(node)

            for nei in adj[node]:
                if nei in seen:
                    continue
                if dfsBob(nei, time + 1):
                    return True

            bobTime.pop(node)
            return False

        def dfsAlice(node, time, income):
            seen.add(node)

            if node not in bobTime or time < bobTime[node]:
                income += amount[node]
            elif time == bobTime[node]:
                income += amount[node] // 2
            
            if len(adj[node]) == 1 and node != 0:
                nonlocal res
                res = max(res, income)
            
            for nei in adj[node]:
                if nei in seen:
                    continue
                dfsAlice(nei, time + 1, income)
        
        dfsBob(bob, 0)

        seen = set()

        dfsAlice(0, 0, 0)

        return res



            