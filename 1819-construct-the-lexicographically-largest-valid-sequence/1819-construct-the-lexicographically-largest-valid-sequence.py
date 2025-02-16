class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        seq_len = (n * 2) - 1
        res = [0 for _ in range(seq_len)]
        used = set()
        def dfs(idx):
            if idx == seq_len:
                return True

            for num in range(n, 0, -1):
                if num in used:
                    continue
                if num > 1 and (idx + num >= seq_len or res[idx + num]):
                    continue

                res[idx] = num
                if num > 1:
                    res[idx + num] = num
                used.add(num)

                j = idx + 1
                while j < seq_len and res[j]:
                    j += 1
                if dfs(j):
                    return True
                used.remove(num)
                res[idx] = 0
                if num > 1:
                    res[idx + num] = 0
            return False
                   
        dfs(0)
        return res