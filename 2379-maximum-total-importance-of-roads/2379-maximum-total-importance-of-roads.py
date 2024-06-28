class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        #Create a heap that has the nodes with the most number of values -> values
        edge_count = [0 for _ in range(n)]
        for i, j in roads:
            edge_count[i] += 1
            edge_count[j] += 1
        heapify(edge_count)

        curr = 1
        res = 0
        while edge_count:
            count = heappop(edge_count)
            res += count * curr
            curr += 1
        return res