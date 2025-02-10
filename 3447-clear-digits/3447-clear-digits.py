class Solution:
    def clearDigits(self, s: str) -> str:
        res = deque([])
        for char in s:
            if ord('0') <= ord(char) <= ord('9'): #We know it's an int
                if res:
                    res.pop()
            else:
                res.append(char)
        return ''.join(res)

