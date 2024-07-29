class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0

        for mid in range(1, len(rating) - 1):
            left_smlr, right_larger = 0, 0
            left_larger, right_smlr = 0, 0
            for i in range(mid):
                if rating[i] < rating[mid]:
                    left_smlr += 1
                else:
                    left_larger += 1
            for i in range(mid + 1, len(rating)):
                if rating[i] < rating[mid]:
                    right_smlr += 1
                else:
                    right_larger += 1
            res += left_smlr * right_larger
            res += left_larger * right_smlr
        return res