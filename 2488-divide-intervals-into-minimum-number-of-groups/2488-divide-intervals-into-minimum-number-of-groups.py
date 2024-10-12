class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start, finish = [], []
        for s, f in intervals:
            heappush(start, s)
            heappush(finish, f)
        i, j = 0, 0
        res = 0
        while start and finish:
            if start[0] > finish[0]:
                j += 1
                heappop(finish)
            else:
                i += 1
                heappop(start)
            res = max(res, i - j)
        return res
            
