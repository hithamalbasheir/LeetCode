class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []
        for num in nums:
            heappush(heap, num)
        
        res = []
        while heap:
            res.append(heappop(heap))
        
        return res