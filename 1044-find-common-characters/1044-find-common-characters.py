class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        #python array of sets
        res = Counter(words[0])
        for word in words[1:]:
            curr = Counter(word)
            for key in res:
                if key not in curr:
                    res[key] = 0
            for key in curr:
                if key in res:
                    res[key] = min(curr[key], res[key])

        final_res = []
        print(res)

        for key, value in res.items():
            if value == 0:
                continue
            for i in range(value):
                final_res.append(key)
        
        return final_res
