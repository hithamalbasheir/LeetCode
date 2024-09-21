class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def dfs(num):
            if num > n:
                return
            res.append(num)
            num *= 10
            for i in range(0, 10):
                dfs(num + i)
        for i in range(1, 10):
            dfs(i)
        return res