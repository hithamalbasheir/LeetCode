class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        #Since the maximum number of 1s for our current bits are 13 bits, we could have 13 buckets and do some insertion sort in each array of the 13 buckets, or we can make it a heap in each of the 13 buckets and pop from it when we're finalizing our result array
        def count_bits(num) -> int:
            count = 0
            while num:
                num &= (num -1)
                count += 1
            return count 

        buckets = [[] for _ in range(14)]

        for num in arr:
            heapq.heappush(buckets[count_bits(num)], num)

        res = []

        for bucket in buckets:
            print(bucket)
            while bucket:
                res.append(heapq.heappop(bucket))
        
        return res