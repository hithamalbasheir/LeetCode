class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #Child's play - custom comparator
        def comparator(a, b):
            if a + b > b + a:
                return -1
            return 1
        
        arr = sorted(list(map(str, nums)), key = cmp_to_key(comparator))

        if arr[0] == '0': return '0'

        return ''.join(arr)