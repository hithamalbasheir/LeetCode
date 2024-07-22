class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heap = []
        for i in range(len(names)):
            heappush(heap, (-heights[i], names[i]))
        
        res = []
        while heap:
            _, name = heappop(heap)
            res.append(name)
        
        return res
