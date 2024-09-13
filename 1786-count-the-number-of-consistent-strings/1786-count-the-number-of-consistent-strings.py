class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        def check_word(word):
            for char in word:
                if char not in allowed:
                    return False
            return True
        allowed = set(allowed)
        res = 0
        for word in words:
            res += check_word(word)
        return res