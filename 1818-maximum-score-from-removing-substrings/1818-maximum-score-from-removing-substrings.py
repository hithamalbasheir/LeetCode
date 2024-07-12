class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pairs(pair, score):
            nonlocal s
            res = 0
            stack = []
            for c in s:
                if c == pair[1] and stack and stack[-1] == pair[0]:
                    stack.pop()
                    res += score
                else:
                    stack.append(c)
            s = "".join(stack)
            return res
        
        res = 0
        (maxi, mini) = ("ab", "ba") if x > y else ("ba", "ab")
        res += remove_pairs(maxi, max(x, y))
        res += remove_pairs(mini, min(x, y))
        return res