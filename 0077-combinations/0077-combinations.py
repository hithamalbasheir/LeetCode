class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        #Decision tree
        def backtrack(start, curr_comb):
            if len(curr_comb) == k:
                res.append(curr_comb[:])
                return
            
            for i in range(start, n+1):
                curr_comb.append(i)
                backtrack(i + 1, curr_comb)
                curr_comb.pop()
        
        backtrack(1, [])
        return res