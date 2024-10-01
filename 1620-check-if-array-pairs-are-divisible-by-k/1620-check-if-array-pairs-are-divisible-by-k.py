class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        #Kinda dumb solution, but to have a full list of pairs, all I need is to match the numbers mod 5 with their compliment
        mod_arr = [0] * k

        for i, num in enumerate(arr):
            rem = num % k
            if rem < 0:
                rem += k
            mod_arr[rem] += 1
        print(mod_arr)
        if mod_arr[0] % 2 != 0: return False
        for i in range(1, (k // 2) + 1):
            if mod_arr[k - i] != mod_arr[i]:
                return False
        return True