class Solution:
    def minimumPushes(self, word: str) -> int:
        occs = Counter(list(word))
        max_heap = []
        for val in occs.values():
            heappush(max_heap, (-val))
        #There should be a math formula for this greedy approach 
        curr_num = 1
        curr_count = 1
        res = 0
        while max_heap:
            res += -heappop(max_heap) * curr_num
            curr_count += 1
            if curr_count == 9:
                curr_count = 1
                curr_num += 1
        return res