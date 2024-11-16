class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        m = len(nums) - k + 1
        for i in range(m):
            prev = 0
            for num in nums[i:i+k]:
                if prev and num - prev != 1:
                    res.append(-1)
                    break
                prev = num
            if len(res) == i:
                res.append(prev)
        return res