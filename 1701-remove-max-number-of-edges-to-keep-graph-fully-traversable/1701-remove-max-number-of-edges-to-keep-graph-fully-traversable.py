class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = list(range(n+1))
        self.rank = [1] * (n+1)

    def find(self, p):
        #Path compression
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return self.parent[p]

    def union(self, p, q):
        p1, q1 = self.find(p), self.find(q)
        if p1 == q1: return 0
        self.count -= 1
        if self.rank[p1] > self.rank[q1]:
            p1, q1 = q1, p1
        self.parent[p1] = q1
        self.rank[q1] += self.rank[p1]
        return 1
    
    def isConnected(self):
        return self.count == 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice, bob = UnionFind(n), UnionFind(n)

        keep = 0

        for t, src, dest in edges:
            if t == 3:
                keep += (alice.union(src, dest) | bob.union(src, dest))

        for t, src, dest in edges:
            if t == 1:
                keep += alice.union(src, dest)
            else:
                keep += bob.union(src, dest)
        
        if bob.isConnected() and alice.isConnected():
            return len(edges) - keep
        return -1