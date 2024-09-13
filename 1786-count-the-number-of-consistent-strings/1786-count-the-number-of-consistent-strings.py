class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        def check_word(word):
            for char in word:
                bit = 1 << ord(char) - ord('a')
                if not bit & mask:
                    return False
            return True
        mask = 0
        for char in allowed:
            bit = 1 << ord(char) - ord('a')
            mask |= bit
        res = 0
        for word in words:
            res += check_word(word)
        return res