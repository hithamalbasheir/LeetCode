class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        #Intervals problem - but solvable with simple logic
        heapify(meetings)
        res = days
        latest_end_day = 0
        while meetings:
            start, end = heappop(meetings)
            busy_days = end - start + 1
            if latest_end_day >= end:
                continue
            elif latest_end_day >= start:
                busy_days = end - latest_end_day
            latest_end_day = end
            res -= busy_days
        return res