# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        i, j = 0, 0
        def dfs():
            nonlocal i, j
            n = TreeNode(preorder[i])
            i += 1
            if n.val != postorder[j]:
                n.left = dfs()
                if n.val != postorder[j]:
                    n.right = dfs()
            j += 1
            return n
        return dfs()