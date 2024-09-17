class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_set = Counter(s1.strip().split())
        s2_set = Counter(s2.strip().split())
        print(s1_set)
        res = []
        for word in s1_set:
            if word not in s2_set and s1_set[word] == 1:
                res.append(word)
        
        for word in s2_set:
            if word not in s1_set and s2_set[word] == 1:
                res.append(word)
        
        return res