class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        #Brute-force
        res = []
        for i, word in enumerate(words):
            for j, target in enumerate(words):
                if j == i: continue
                if word in target:
                    res.append(word)
                    break
        return res