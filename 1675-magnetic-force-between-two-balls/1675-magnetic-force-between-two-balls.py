class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        #Go from the lowest possible force greedily up to the 
        low, high = 1, position[-1] - position[0]

        def valid(target):
            balls, prev_basket = 0, -10 ** 30
            for b in position:
                if b - prev_basket >= target:
                    balls += 1
                    prev_basket = b
            
            return balls >= m
        
        while low < high:
            mid = (high + low + 1) // 2

            if valid(mid):
                low = mid
            else:
                high = mid - 1

        return low