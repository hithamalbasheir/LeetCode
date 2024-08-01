class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for entry in details:
            if int(entry[11:13]) > 60:
                res += 1
        return res