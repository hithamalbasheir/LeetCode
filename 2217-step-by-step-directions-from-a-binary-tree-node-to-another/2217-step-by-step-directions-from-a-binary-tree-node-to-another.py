# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node, path, target):
            if not node:
                return ""
            if node.val == target:
                return path
            
            path.append("L")
            res = dfs(node.left, path, target)
            if res: return res

            path.pop()
            path.append("R")
            res = dfs(node.right, path, target)
            if res: return res

            path.pop()
            return ""
        
        src = dfs(root, [], startValue)
        dest = dfs(root, [], destValue)

        i = 0
        while i < min(len(src), len(dest)):
            if src[i] != dest[i]:
                break
            i += 1
        return "".join(['U'] * len(src[i:]) + dest[i:])