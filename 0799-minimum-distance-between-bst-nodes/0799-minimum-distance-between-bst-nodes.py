# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans = float('inf')
        pred = None
        def dfs(root):
            nonlocal ans, pred
            if not root:
                return
            dfs(root.left)
            if pred is not None:
                ans = min(ans, root.val - pred)
            pred = root.val
            dfs(root.right)
        dfs(root)
        return ans
        