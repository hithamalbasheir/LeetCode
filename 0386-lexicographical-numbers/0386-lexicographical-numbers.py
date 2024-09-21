class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def dfs(num):
            if num > n:
                return
            res.append(num)
            for i in range(0, 10):
                dfs(int(str(num) + str(i)))
        for i in range(1, 10):
            dfs(i)
        return res