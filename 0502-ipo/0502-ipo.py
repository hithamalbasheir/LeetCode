class Solution:
    def findMaximizedCapital(self, k: int, c: int, profits: List[int], capitals: List[int]) -> int:
        n = len(capitals)
        capitals_heap = []
        for i in range(n):
            heapq.heappush(capitals_heap, [capitals[i], i])

        max_profits_heap = []
        for _ in range(k):
            while capitals_heap and capitals_heap[0][0] <= c:
                i = heapq.heappop(capitals_heap)[1]
                heapq.heappush(max_profits_heap, [-profits[i], i])
            if not max_profits_heap:
                break
            c += abs(heapq.heappop(max_profits_heap)[0])
        return c

