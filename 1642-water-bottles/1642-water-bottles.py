class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        empty = 0
        full = numBottles
        while full > 0:
            res += full
            bottles = empty + full
            full = bottles // numExchange
            empty = bottles % numExchange
        return res