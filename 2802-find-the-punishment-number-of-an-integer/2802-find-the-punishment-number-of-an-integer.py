class Solution:
    def punishmentNumber(self, n: int) -> int:
        def partition(i, curr, target, str_num):
            if i == len(str_num) and curr == target:
                return True
            
            for j in range(i, len(str_num)):
                if partition(j + 1, curr + int(str_num[i:j+1]), target, str_num):
                    return True
            return False
        
        res = 0
        for i in range(1, n + 1):
            if partition(0, 0, i, str(i * i)):
                res += i * i
        return res