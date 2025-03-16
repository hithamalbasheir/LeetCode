class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        memo = defaultdict(list)
        for i, num in enumerate(nums):
            memo[num].append(i)
        m = len(nums)
        res = [-1 for _ in range(len(queries))]
        for i, query in enumerate(queries):
            num = nums[query]
            n = len(memo[num])
            if n <= 1:
                continue
            left, right = 0, n - 1
            idx = -1
            while left < right:
                mid = (left + right + 1) // 2
                if memo[num][mid] == query:
                    idx = mid
                    break
                if memo[num][mid] > query:
                    right = mid - 1
                else:
                    left = mid
            idx = left if idx < 0 else idx
            pre = memo[num][idx - 1]
            pre_dist = min(abs(query - pre), abs(m - pre + query))
            post = memo[num][(idx + 1) % n]
            post_dist = min(abs(m - query + post), abs(post - query))
            res[i] = min(post_dist, pre_dist)
        return res
        