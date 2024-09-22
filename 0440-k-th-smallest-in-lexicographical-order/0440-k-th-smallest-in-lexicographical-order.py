class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        #I'm way too lazy to write a new solution so I'll just use LC - optimized!
        def get_steps(curr):
            res = 0
            num = curr
            next_num = curr + 1
            while num <= n:
                res += min(n + 1, next_num) - num
                num *= 10
                next_num *= 10
            return res
        
        curr = 1
        idx = 1
        while idx < k:
            steps = get_steps(curr)
            if idx + steps <= k:
                curr += 1
                idx += steps
            else:
                curr *= 10
                idx += 1
        return curr