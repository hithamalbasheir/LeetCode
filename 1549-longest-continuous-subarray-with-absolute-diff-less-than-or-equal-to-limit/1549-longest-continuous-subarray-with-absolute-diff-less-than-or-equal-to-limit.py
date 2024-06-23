class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_heap = []
        max_heap = []
        left = 0
        res = 0
        for right, num in enumerate(nums):
            heappush(min_heap, (num, right))
            heappush(max_heap, (-num, right))
            while (-max_heap[0][0] - min_heap[0][0]) > limit:
                left = min(max_heap[0][1], min_heap[0][1]) + 1
                while max_heap[0][1] < left:
                    heappop(max_heap)
                while min_heap[0][1] < left:
                    heappop(min_heap)
            res = max(res, right - left + 1)
        return res