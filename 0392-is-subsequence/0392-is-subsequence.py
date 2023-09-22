class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #Two pointer on two lists, go on comparing both lists till I find all equal elements then return true, otherwise return false
        #edge case
        if not s:
            return True
        s_ptr, t_ptr = 0, 0
        while s_ptr < len(s) and t_ptr < len(t):
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
                if s_ptr == len(s):
                    return True
            t_ptr += 1
        return False
        