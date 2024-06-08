class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen_mods = {0: -1}
        prefix = 0
        for i, num in enumerate(nums):
            prefix = (prefix + num) % k
            if prefix in seen_mods:
                if i - seen_mods[prefix] > 1:
                    return True
            else:
                seen_mods[prefix] = i
        return False