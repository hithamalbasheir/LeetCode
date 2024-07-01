class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        odds = 0
        for num in arr:
            if num % 2 == 0: 
                odds = 0
                continue
            odds += 1
            if odds >= 3:
                return True
        
        return False