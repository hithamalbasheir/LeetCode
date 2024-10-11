class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        heap = []
        for i, time in enumerate(times):
            heappush(heap, (time[0], time[1], i))
        chairs = [1 for _ in range(len(times))]
        out_heap = []
        while heap:
            start, finish, idx = heappop(heap)
            while out_heap and out_heap[0][0] <= start:
                _, time = heappop(out_heap)
                chairs[time] = 1
            for i, val in enumerate(chairs):
                if val:
                    if targetFriend == idx:
                        return i
                    chairs[i] = 0
                    heappush(out_heap, (finish, i))
                    break
        return 0
            
            