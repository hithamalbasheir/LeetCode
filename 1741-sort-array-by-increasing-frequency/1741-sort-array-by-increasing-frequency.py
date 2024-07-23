class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        heap = []
        for num, freq in count.items():
            heappush(heap, (freq, -num))
        
        res = []
        while heap:
            freq, num = heappop(heap)
            res.extend([-num] * freq)
        
        return res