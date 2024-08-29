class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows, cols = defaultdict(list), defaultdict(list)
        for i, j in stones:
            rows[i].append(j)
            cols[j].append(i)
        
        res = 0
        seen = set()
        for i, j in stones:
            if (i, j) not in seen:
                seen.add((i, j))
                q = deque([(i, j)])
                while q:
                    curr_i, curr_j = q.popleft()
                    for nbr_j in rows[curr_i]:
                        if (curr_i, nbr_j) not in seen:
                            seen.add((curr_i, nbr_j))
                            q.append((curr_i, nbr_j))
                        
                    for nbr_i in cols[curr_j]:
                        if (nbr_i, curr_j) not in seen:
                            seen.add((nbr_i, curr_j))
                            q.append((nbr_i, curr_j))
                res += 1
        return len(stones) - res
