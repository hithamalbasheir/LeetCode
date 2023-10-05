class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #I'll count all the elments in the array
        #I'll then loop through them and divide the count of the current number over the total number of the array length, and if it does 
        count = Counter(nums)
        print(count)
        res = []
        for i in count:
            if (count[i]/len(nums)) > 0.333334:
                res.append(i)
        return res
