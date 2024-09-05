class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        curr_sum = sum(rolls)
        total = len(rolls) + n
        missing_sum = -curr_sum + total * mean
        if not (1 <= missing_sum / n <= 6):
            return []
        if n == missing_sum:
            return [1] * n
        if missing_sum / 6 == n:
            return [6] * n
        res = []
        while n > 0 and missing_sum > n:
            print(missing_sum)
            num = 6 if (missing_sum - 6) >= n else missing_sum - n + 1
            missing_sum -= num
            res.append(num)
            n -= 1
        if n > 0:
            res.extend([1 for _ in range(n)])
        return res