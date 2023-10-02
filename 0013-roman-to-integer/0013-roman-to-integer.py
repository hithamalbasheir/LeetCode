class Solution:
    def romanToInt(self, s: str) -> int:
        nums_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = 0
        prev = float('inf')
        for ch in s:
          num = nums_map[ch]
          if num > prev:
            res -= 2 * prev
          res += num
          prev = num
        return res