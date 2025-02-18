class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        seen = set()
        res = [0] * (n + 1)
        def backtrack(i):
            nonlocal res
            if i == n + 1:
                return True
            if pattern[i - 1] == 'I' and res[i - 1] == '9':
                return False
            if pattern[i - 1] == 'D' and res[i - 1] == '1':
                return False
            upper = 10 if pattern[i - 1] == 'I' else int(res[i - 1])
            lower = 1 if pattern[i - 1] == 'D' else int(res[i - 1]) + 1
            for j in range(lower, upper):
                if j in seen:
                    continue
                res[i] = str(j)
                seen.add(j)
                if backtrack(i + 1):
                    return True
                seen.remove(j)
                res[i] = 0
            return False
        
        for i in range(1,10):
            seen.add(i)
            res[0] = str(i)
            if backtrack(1):
                return ''.join(res)
            res[0] = 0
            seen.remove(i)
        return []