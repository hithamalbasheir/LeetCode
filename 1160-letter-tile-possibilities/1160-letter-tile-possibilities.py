class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        #backtracking
        seen = set()
        char_set = Counter(tiles)
        def backtrack(i, seq):
            if i == len(tiles):
                return
            if seq in seen:
                return
            seen.add(seq)
            for char in tiles:
                if char_set[char] == 0:
                    continue
                char_set[char] -= 1
                backtrack(i + 1, seq + (char))
                char_set[char] += 1
        for char in tiles:
            if char in seen:
                continue
            char_set[char] -= 1 
            backtrack(0, (char))
            char_set[char] += 1
        return len(seen)
