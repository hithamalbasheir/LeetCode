class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_num, max_num = [], []
        for i, arr in enumerate(arrays):
            heappush(min_num, (arr[0], i))
            heappush(max_num, (-arr[-1], i))
        while min_num:
            sml, i = heappop(min_num)
            big, j = heappop(max_num)
            if i == j:
                max_diff = abs(big - max_num[0][0])
                min_diff = abs(sml - min_num[0][0])
                if max_diff > min_diff:
                    heappush(max_num, (big, j))
                else:
                    heappush(min_num, (sml, i))
            else:
                return abs(-big - sml)
        return 0