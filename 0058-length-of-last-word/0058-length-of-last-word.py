class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idk = s.strip().split(" ")
        return len(idk[-1])