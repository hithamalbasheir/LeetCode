class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        memo = Counter(arr1)
        res = []
        for num in arr2:
            for i in range(memo[num]):
                res.append(num)
            memo.pop(num)
        arr1.sort()
        for num in arr1:
            if num in memo:
                res.append(num)
        return res