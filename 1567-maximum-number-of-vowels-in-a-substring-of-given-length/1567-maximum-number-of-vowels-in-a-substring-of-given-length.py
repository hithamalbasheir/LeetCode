class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #Create a set with vowels
        #Process the string with left and right pointers
        #keep comparing to maximize the number
        vowels = set(['a','i','e','o','u'])
        l, r = 0, 0
        curr_sum = 0
        curr_max = 0
        curr_win = 1
        while r < len(s):
            if s[r] in vowels:
                curr_sum += 1
            if curr_win == k:
                curr_max = max(curr_sum, curr_max)
                if s[l] in vowels:
                    curr_sum -= 1
                l += 1
                curr_win -= 1
            r += 1
            curr_win += 1
        return curr_max
                
        