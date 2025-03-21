class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        #Hashing
        res = defaultdict(int)
        for char in arr:
            res[char] += 1
        
        i = 1
        for key in res:
            if res[key] > 1:
                continue
            if k == i:
                return key
            i += 1
        return ''