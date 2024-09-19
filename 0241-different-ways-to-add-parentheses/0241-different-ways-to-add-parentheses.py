class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operations = {
            '+' : lambda a, b : a + b,
            '-' : lambda a, b : a - b,
            '*' : lambda a, b : a * b
        }

        def dfs(left, right): 
            res = []

            for i in range(left, right + 1):
                op = expression[i]
                if op in operations:
                    left_side = dfs(left, i - 1)
                    right_side = dfs(i + 1, right)

                    for n1 in left_side:
                        for n2 in right_side:
                            res.append(operations[op](n1, n2))
            if not res:
                res.append(int(expression[left:right + 1]))
            return res
        
        return dfs(0, len(expression) - 1)