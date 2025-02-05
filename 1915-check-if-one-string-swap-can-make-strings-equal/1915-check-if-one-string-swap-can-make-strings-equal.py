class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        #We have to make sure of 2 things, both the strings have the same set of characters, and that there's at most one diff
        #But this will require extra space to check that both of them are equal in terms of chars, so we can just store the first diff and then use that to ensure the second diff complements the first diff, anything other than this is False
        diff_count = 0
        first_char, second_char = None, None
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            if diff_count == 2:
                return False
            if diff_count == 0:
                diff_count += 1
                first_char, second_char = s2[i], s1[i]
                continue
            diff_count += 1
            if first_char != s1[i] or second_char != s2[i]:
                return False
        return diff_count % 2 == 0