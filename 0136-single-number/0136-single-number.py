class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Given that when every number gets Xored by itself will result in 0 and that when every number is Xored by 0 will result the same number then we can conclude that if we xored all elements we will end up with the single number!
        res = 0
        for num in nums:
            res ^= num
        return res 
        