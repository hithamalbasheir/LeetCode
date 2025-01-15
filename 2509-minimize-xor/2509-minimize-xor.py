class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        #To be able to get the minimum possible xor, we'll have to get rid of the most significant bits, and then if I get a left over, I'll just put it in the beginnning lines
        res = 0
        num_bits = bin(num2)[2:].count('1')
        for i in reversed(range(31)):
            if num_bits == 0:
                break
            if num1 & (1 << i):
                res |= 1 << i
                num_bits -= 1
        
        for i in range(32):
            if num_bits == 0:
                break
            if not (res & (1 << i)):
                res |= 1 << i
                num_bits -= 1
        return res