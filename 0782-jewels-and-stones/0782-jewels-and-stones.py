class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_map = Counter(jewels)
        res = 0
        for stone in stones:
            if stone in jewels_map:
                res += 1
        return res
        