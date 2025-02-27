class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        seen = set()
        nums = set(arr)
        res = 0
        for i, num in enumerate(arr):
            for j in range(i + 1, len(arr)):
                if (i, j) in seen:
                    continue
                seen.add((i,j))
                prev, curr = num, arr[j]
                curr_len = 2
                while (temp := (prev + curr)) in nums:
                    prev, curr = curr, temp
                    curr_len += 1
                    res = max(res, curr_len)
        return res