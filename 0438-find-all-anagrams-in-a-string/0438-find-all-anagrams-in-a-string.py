class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p:
            return []
        target_count = Counter(p)
        curr_window = defaultdict(int)
        left = 0
        res = []
        for right in range(len(s)):
            char = s[right]
            if char not in target_count:
                left = right + 1
                curr_window = defaultdict(int)
                continue
            curr_window[char] += 1
            char = s[left]
            while left < right and ((target_count[char] < curr_window[char])):
                curr_window[char] -= 1
                if curr_window[char] == 0:
                    curr_window.pop(char)
                left += 1
                char = s[left]
            if curr_window == target_count:
                res.append(left)
        return res
            
