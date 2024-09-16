class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert_to_minutes(timePoint: str) -> int:
            hours, minutes = map(int, timePoint.split(':'))
            return hours * 60 + minutes

        sorted_points = []
        for time in timePoints:
            sorted_points.append(convert_to_minutes(time))
        sorted_points.sort()
        #1440 minutes a day - max difference between 2 times is 720 minutes
        res = 720
        for i, point in enumerate(sorted_points):
            prev = sorted_points[i - 1]
            if prev == point: return 0
            time_diff = min((abs(point - prev) % 1440), 1440 - abs(point - prev)) 
            res = min(res, time_diff)
        return res
