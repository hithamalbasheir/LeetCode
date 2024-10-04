class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        groups = len(skill) // 2
        target = sum(skill) // groups

        n = len(skill)
        
        res = 0
        left = 0
        for right in range(n - 1, n//2 - 1, -1):
            if skill[left] + skill[right] != target:
                return -1
            res += skill[left] * skill[right]
            left += 1
        
        return res

        # counter = Counter(skill)
        # res = 1
        # groups = len(skill) // 2
        # target = sum(skill) // groups
        # for key in skill:
        #     if key not in counter: continue
        #     curr_val = counter[key]
        #     for _ in range(counter[key]):
        #         counter[key] -= 1
        #         if counter[key] == 0:
        #             counter.pop(key)
        #         if rem := target - curr_val in counter:
        #             counter[rem] -= 1
        #             if counter[rem] == 0:
        #                 counter.pop(rem)
        #             res *= rem * curr_val
        #             if curr_val not in counter: break
        #         else:
        #             return -1
        # return res