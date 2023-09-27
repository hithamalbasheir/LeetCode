class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        #What an idiot I am trying to actually construct all the string, instead I can only count the length of the final array and then do some basic maths to solve it

        #Get the length
        length = 0
        for char in s:
            if char.isdigit():
                length *= int(char)
            else:
                length += 1
        
        #Do some comparisons in a reverse order to get the char at Kth pos
        for char in reversed(s):
            k %= length
            if k == 0 and char.isalpha():
                return char
            elif char.isdigit():
                length //= int(char)
            else:
                length -= 1
        
        return ''