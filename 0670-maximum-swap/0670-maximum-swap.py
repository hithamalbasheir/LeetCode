class Solution:
    def maximumSwap(self, num: int) -> int:
        nums_heap = []
        nums = [int(i) for i in str(num)]
        nums_map = {j: i for i, j in enumerate(nums)}
        for i in nums:
            heappush(nums_heap, -i)
        for i in range(len(nums)):
            curr = -heappop(nums_heap)
            if curr != nums[i]:
                nums[i], nums[nums_map[curr]] = curr, nums[i]
                break
        return int("".join([str(i) for i in nums]))