class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        chars_heap = []
        chars = ['a', 'b', 'c']
        for i, char in enumerate([a, b, c]):
            if char > 0:
                heappush(chars_heap, (-char, chars[i]))
        curr_char_count = 0
        prev_char = None
        res = []
        print(chars_heap)
        while chars_heap:
            count, char = heapq.heappop(chars_heap)
            # If previous character was the same and used twice consecutively, we need to choose another one
            if prev_char == char and prev_char_count == 2:
                if not chars_heap:
                    break  # No more characters to use
                count_2, char_2 = heapq.heappop(chars_heap)
                res.append(char_2)
                if count_2 < -1:
                    heapq.heappush(chars_heap, (count_2 + 1, char_2))
                heapq.heappush(chars_heap, (count, char))
                prev_char = char_2
                prev_char_count = 1
            else:
                # Use the current character
                res.append(char)
                if count < -1:
                    heapq.heappush(chars_heap, (count + 1, char))
                if prev_char == char:
                    prev_char_count += 1
                else:
                    prev_char = char
                    prev_char_count = 1
        return "".join(res)