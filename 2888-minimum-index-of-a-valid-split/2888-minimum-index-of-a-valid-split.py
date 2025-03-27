class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        first_split = defaultdict(int)
        second_split = Counter(nums)

        for i, num in enumerate(nums):
            second_split[num] -= 1
            first_split[num] += 1
            dom_1 = first_split[num] * 2 > i + 1
            dom_2 = second_split[num] * 2 > len(nums) - i - 1
            if dom_1 and dom_2:
                return i
        return -1