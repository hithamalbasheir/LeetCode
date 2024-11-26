class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegrees = [0 for _ in range(n)]

        for src, dest in edges:
            indegrees[dest] += 1

        res = -1
        print(indegrees)
        for i, j in enumerate(indegrees):
            if j == 0:
                if res >= 0: return -1
                res = i
        return res