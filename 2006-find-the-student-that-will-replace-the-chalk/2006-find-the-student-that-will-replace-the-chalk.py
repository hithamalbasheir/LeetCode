class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        if len(chalk) == 1: return 0
        chalk_sum = sum(chalk)
        while k >= chalk_sum:
            k -= chalk_sum
        for i, num in enumerate(chalk):
            if num > k:
                return i
            k -= num
        return len(num) - 1