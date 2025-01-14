class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        a_memo, b_memo = set(), set()
        intersection = set()
        for i, num in enumerate(A):
            a_memo.add(num)
            b_memo.add(B[i])
            if num in b_memo:
                intersection.add(num)
            if B[i] in a_memo:
                intersection.add(B[i])
            res.append(len(intersection))
        return res
        