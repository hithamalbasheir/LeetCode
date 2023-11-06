class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_count, mag_count = Counter(ransomNote), Counter(magazine)
        for key in r_count:
            if key not in mag_count or mag_count[key] < r_count[key]:
                return False
        return True