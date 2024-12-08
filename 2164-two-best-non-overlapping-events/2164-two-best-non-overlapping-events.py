class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x: x[1])

        max_until = []
        max_val = 0
        for _, end, val in events:
            max_val = max(max_val, val)
            max_until.append((end, max_val))
        
        res = 0
        for start, end, val in events:
            res = max(res, val)
            idx = bisect_left(max_until, (start, 0)) - 1
            if idx >= 0:
                res = max(res, val + max_until[idx][1])
                
        return res