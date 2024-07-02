class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        heapify(nums1)
        heapify(nums2)
        res = []
        while nums1 and nums2:
            num1, num2 = heappop(nums1), heappop(nums2)
            if num1 == num2:
                res.append(num1)
                continue
            if num1 > num2:
                heappush(nums1, num1)
                continue
            heappush(nums2, num2)
        return res