class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        #Since XOR will cancel each other if it's of even length, then we need to check if both arrays are of even length, if not the xor of only one of them if the other is even, if not the result is the xor of all of them
        n1, n2 = len(nums1), len(nums2)
        if n1%2 == 0 and n2%2 == 0:
            return 0
        
        if not (n1 & 1):
            res = 0
            for num in nums1:
                res ^= num
            return res
        
        if not (n2 & 1):
            res = 0
            for num in nums2:
                res ^= num
            return res

        res = 0
        for num in nums1:
            res ^= num
        for num in nums2:
            res ^= num
        return res