class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        #Recursion - no memoization
        
        #Base case, where we have more than 12 digits
        if len(s) > 12:
            return []
        
        res = []

        #Where all the magic happens
        def backtrack(i, dots, ip):
            if dots == 4 and i == len(s):
                res.append(ip[:-1])
                return
            if dots > 4:
                return
            for j in range(i, min(i + 3, len(s))): #in case the string ends before i
                curr_seg = s[i:j+1]
                if int(curr_seg) <= 255 and (curr_seg[0] != '0' or curr_seg == '0'):
                    backtrack(j + 1, dots + 1, ip + curr_seg + ".")

        backtrack(0, 0, "")
        return res