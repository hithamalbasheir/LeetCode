class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        #kinda heap, hash table problem, although it seems a graph problem at first glance
        heap = []
        for idx, num in enumerate(nums):
            numVal = []
            for i in str(num):
                numVal.append(str(mapping[int(i)]))
            numVal = ''.join(numVal)
            heappush(heap, (int(numVal), idx, num))
        
        res = []
        while heap:
            _, __, num = heappop(heap)
            res.append(num)
        
        return res