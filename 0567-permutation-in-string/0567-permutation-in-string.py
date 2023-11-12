class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        perm = Counter(s1)
        for i in range(len(s2) - len(s1) + 1):
            if s2[i] not in perm:
                continue
            temp = perm.copy()
            start = i
            while start < len(s2) and s2[start] in temp:
                char = s2[start]
                temp[char] -= 1
                if temp[char] == 0:
                    temp.pop(char)
                start += 1
            if not temp:
                return True
        return False