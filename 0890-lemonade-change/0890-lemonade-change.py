class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)
        for bill in bills:
            if bill == 5:
                change[5] += 1
            elif bill == 10:
                if not change[5]:
                    return False
                change[10] += 1
                change[5] -= 1
            else:
                if (not change[10] and not change[5]) or not change[5]:
                    return False
                if not change [10] and change[5] < 3:
                    return False
                if change[10]:
                    change[10] -= 1
                    change[5] -= 1
                else:
                    change[5] -= 3
        return True