class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = 0
        start = 0
        for begin, period in customers:
            end = begin + period
            end += start - begin if begin < start else 0
            total += end - begin
            start = end
        return total / len(customers)
