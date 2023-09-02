class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #Look for the current word starting letter 
        #start a dfs approach on all possible paths as long as it's matching my word
        #If I found the word I'll return true, else I'll traverse till the last letter returning False in the end
        col_len = len(board) - 1
        row_len = len(board[0]) - 1
        path = set()
        def dfs(i, j, char_idx):
            if char_idx == len(word):
                return True
            if i < 0 or i > col_len or j < 0 or j > row_len or (i, j) in path or word[char_idx] != board[i][j]:
                return False
            path.add((i,j))
            res = dfs(i-1, j, char_idx + 1) or dfs(i+1, j, char_idx + 1) or dfs(i, j+1, char_idx + 1) or dfs(i, j-1, char_idx + 1)
            path.remove((i,j))
            return res
        result = False
        for i in range(col_len+1):
            for j in range(row_len+1):
                if word[0] == board[i][j]:
                    result = result or dfs(i, j, 0)
        return result