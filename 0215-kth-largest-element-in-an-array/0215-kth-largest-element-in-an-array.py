class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Quick select (Worst case not as good as using a heap or normal sorting, but an average case of O(n))
        k = len(nums) - k
        def quick_select(l, r):
            piv, ptr = nums[r], l
            for i in range(l, r):
                if nums[i] <= piv:
                    nums[i], nums[ptr] = nums[ptr], nums[i]
                    ptr += 1
            nums[r], nums[ptr] = nums[ptr], nums[r]

            if ptr < k:
                return quick_select(ptr+1, r)
            elif ptr > k:
                return quick_select(l, ptr - 1)
            else:
                return piv
        return quick_select(0, len(nums) - 1)