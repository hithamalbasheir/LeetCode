class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_counter = Counter(s1)
        curr_window = {}
        for i, char in enumerate(s2):
            curr_window[char] = curr_window.get(char, 0) + 1
            if i < len(s1): continue
            left_char = s2[i - len(s1)]
            curr_window[left_char] -= 1
            if curr_window[left_char] == 0:
                curr_window.pop(left_char)
                
            if curr_window == target_counter:
                return True
        return False