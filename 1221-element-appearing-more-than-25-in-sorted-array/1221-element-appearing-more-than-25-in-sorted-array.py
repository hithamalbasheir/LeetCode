class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        special = len(arr)//4
        count = 1
        prev = arr[0]
        for i in range(1, len(arr)):  
            if prev != arr[i]:
                count = 1
            else:
                count += 1
            prev = arr[i]
            if count > special:
                return arr[i]
        return prev     