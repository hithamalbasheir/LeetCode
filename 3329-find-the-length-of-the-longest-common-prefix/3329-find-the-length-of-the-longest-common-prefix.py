class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_set = set()

        for num in arr1:
            while num > 0 and num not in prefix_set:
                prefix_set.add(num)
                num //= 10
        
        res = 0
        for num in arr2:
            while num > 0 and num not in prefix_set:
                num //= 10
            
            if num in prefix_set:
                res = max(res, len(str(num)))
        return res