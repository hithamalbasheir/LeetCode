class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = sorted([(r[0], r[2]) for r in rectangles])
        y = sorted([(r[1], r[3]) for r in rectangles])

        def valid_cuts(intervals):
            prev_end = -1
            count = 0
            for start, end in intervals:
                if start >= prev_end:
                    count += 1
                prev_end = max(end, prev_end)
                if count >= 3: #Early exit
                    return True
            return count >= 3

        return valid_cuts(x) or valid_cuts(y)