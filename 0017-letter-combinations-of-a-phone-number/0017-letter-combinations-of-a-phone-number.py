class Solution:
    #Constant time lookup
    buttons = {
		"2":"abc", "3": "def", "4": "ghi", 
		"5": "jkl","6": "mno", "7": "pqrs", 
		"8": "tuv", "9": "wxyz",
	}
    def letterCombinations(self, digits: str) -> List[str]:
        #Recursive approach!
        res = []
        def dfs(depth, comb):
            if len(comb) >= len(digits):
                if comb:
                    res.append(comb)
                return
            curr_chars = self.buttons[digits[depth]]
            for char in curr_chars:
                dfs(depth + 1, comb + char)
        
        dfs(0, "")
        return res