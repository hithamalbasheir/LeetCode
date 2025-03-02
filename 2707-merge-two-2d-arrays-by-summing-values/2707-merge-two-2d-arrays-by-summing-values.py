class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = defaultdict(int)

        for i in range(max(len(nums1), len(nums2))):
            if i < len(nums1):
                id1, num1 = nums1[i]
                res[id1] += num1
            if i < len(nums2):
                id2, num2 =  nums2[i]
                res[id2] += num2
        return [[i, num] for i, num in sorted(res.items())]