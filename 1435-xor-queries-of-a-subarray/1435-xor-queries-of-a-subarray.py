class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        prefix = [0]
        for num in arr:
            xor = prefix[-1] ^ num
            prefix.append(xor)
        for left, right in queries:
            num = prefix[left] ^ prefix[right + 1]
            res.append(num)
        return res