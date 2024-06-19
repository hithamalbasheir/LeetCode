class Solution:
    def get_num_of_bouquets(self, bloomDay: List[int], m: int, k: int) -> int:
        res = 0
        boq_num = 0
        for day in bloomDay:
            if day <= m:
                res += 1
            else:
                res = 0

            if res == k:
                boq_num += 1
                res = 0
        return boq_num

    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1

        start = 0
        end = max(bloomDay)
        minDays = -1

        while start <= end:
            mid = (start + end) // 2

            if self.get_num_of_bouquets(bloomDay, mid, k) >= m:
                minDays = mid
                end = mid - 1
            else:
                start = mid + 1

        return minDays