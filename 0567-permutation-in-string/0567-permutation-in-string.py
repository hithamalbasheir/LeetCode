class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Optimized sliding window approach
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        curr_window = {}

        for i, char in enumerate(s2):
            #Add current char to window counter
            curr_window[char] = curr_window.get(char, 0) + 1

            #Remove the char on the left out of the window
            if i >= len(s1):
                left_char = s2[i - len(s1)]
                curr_window[left_char] -= 1
                if curr_window[left_char] == 0:
                    curr_window.pop(left_char)
            
            if curr_window == s1_count:
                return True
                
        return False