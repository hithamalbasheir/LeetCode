class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        res = 0 
        ptr = 0
        for i in nums:
            while n > ptr and i > ptr + 1:
                ptr += ptr + 1
                res += 1
            ptr += i
        
        while n > ptr:
            ptr += ptr + 1
            res += 1

        return res