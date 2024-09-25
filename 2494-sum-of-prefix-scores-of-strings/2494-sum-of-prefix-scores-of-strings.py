class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefix_map = {}
        
        def get_prefixes(word):
            res = []
            for i in range(len(word)):
                res.append(word[:i+1])
            return res
        
        for word in words:
            prefixes = get_prefixes(word)
            for prefix in prefixes:
                prefix_map[prefix] = prefix_map.get(prefix, 0) + 1
        
        res = [0 for _ in range(len(words))]

        for i, word in enumerate(words):
            prefixes = get_prefixes(word)
            for prefix in prefixes:
                res[i] += prefix_map[prefix]
        
        return res
