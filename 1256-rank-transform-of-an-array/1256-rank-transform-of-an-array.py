class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        loc = defaultdict(list)
        for i, num in enumerate(arr):
            loc[num].append(i)
        res = [0] * len(arr)
        
        arr.sort()
        rank = 1
        for num in arr:
            if not loc: break
            if num not in loc: #We've already computed it
                continue
            for idx in loc[num]:
                res[idx] = rank
            loc.pop(num)
            rank += 1
        return res