class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums = re.findall(r'[+-]?\d+', expression)
        print(nums)
        nums = [int(num) for num in nums]
        numer = 0
        denomin = 1

        for i in range(0, len(nums), 2):
            num, den = nums[i], nums[i + 1]
            numer *= den 
            numer += num * denomin
            denomin *= den
        
        common_divisor = gcd(numer, denomin)
        return f"{numer // common_divisor}/{denomin // common_divisor}"