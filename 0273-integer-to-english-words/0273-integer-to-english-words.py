class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        res = ''
        ones_map = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens_map = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", " Thousand", " Million", " Billion"]

        def get_num(n):
            res = []
            hunds = n // 100
            if hunds:
                res.append(ones_map[hunds] + " Hundred")
            rem = n % 100

            if rem >= 20:
                tens, ones = rem // 10, rem % 10
                res.append(tens_map[tens])
                if ones:
                    res.append(ones_map[ones])
            elif rem:
                res.append(ones_map[rem])
            
            return " ".join(res)

        i = 0
        res = []

        while num:
            digits = num % 1000
            s = get_num(digits)
            if s:
                res = [s + thousands[i]] + res
            num //= 1000
            i += 1
        return " ".join(res)