class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res_str = ''
        res = ''
        for char in s:
            order = ord(char) - ord('a') + 1
            res += str(order)
        res = int(res)
        for _ in range(k):
            res = sum(int(num) for num in str(res))
            
        return res