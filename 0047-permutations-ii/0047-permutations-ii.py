class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def recurse(comb, counter):
            if (len(comb) == len(nums)):
                res.append(comb[:])
                return 

            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1

                    recurse(comb, counter)

                    comb.pop()
                    counter[num] += 1
        
        recurse([], Counter(nums))

        return res

