class Solution:
    def minDifference(self, nums: List[int]) -> int:
        #Two heaps
        if len(nums) <= 4: return 0
        minFour = sorted(nsmallest(4,nums))
        maxFour = sorted(nlargest(4,nums))

        res = float('inf')
        for i in range(4):
            res = min(res,maxFour[i]-minFour[i])
        return res