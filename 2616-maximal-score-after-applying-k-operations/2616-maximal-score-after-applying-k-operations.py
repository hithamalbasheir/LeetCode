class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-i for i in nums]
        heapify(heap)
        res = 0
        for _ in range(k):
            num = -heappop(heap)
            res += num
            heappush(heap, -ceil(num / 3))
        return res