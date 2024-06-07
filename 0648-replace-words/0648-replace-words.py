class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        memo = set(dictionary)
        words = sentence.split(" ")
        for pos, word in enumerate(words):
            prefix = ''
            i = 0
            while prefix not in memo and i < len(word):
                prefix += word[i]
                i += 1
            if prefix != word:
                words[pos] = prefix
        return " ".join(words)