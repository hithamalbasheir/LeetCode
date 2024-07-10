class Solution:
    def minOperations(self, logs: List[str]) -> int:
        lvl = 0
        up, stay = '../', './'
        for log in logs:
            if log == up:
                lvl -= 1 if lvl > 0 else 0
            elif log == stay:
                continue
            else:
                lvl += 1
        return lvl