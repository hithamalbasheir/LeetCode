class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = deque([])

        for char in expression:
            if char == ')':
                inner = []
                while stack[-1] != '(':
                    inner.append(stack.pop())
                stack.pop()
                operator = stack.pop()
            
                if operator == '!':
                    res = inner[0] == 'f'
                elif operator == '&':
                    res = all(val == 't' for val in inner)
                elif operator == '|':
                    res = any(val == 't' for val in inner)
                
                stack.append('t' if res else 'f')
            elif char not in (',', ' '):
                stack.append(char)
        
        return stack.pop() == 't'