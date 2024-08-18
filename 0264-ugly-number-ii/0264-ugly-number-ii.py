class Solution:
    def nthUglyNumber(self, n: int) -> int:
        prime_nums = set([2,3,5])
        heap = [1]
        seen = set([1])
        ugly_num = 0
        
        for _ in range(n):
            curr_num = heappop(heap)
            for num in prime_nums:
                ugly_num = curr_num * num
                if ugly_num not in seen:
                    heappush(heap, ugly_num)
                    seen.add(ugly_num)
        return curr_num