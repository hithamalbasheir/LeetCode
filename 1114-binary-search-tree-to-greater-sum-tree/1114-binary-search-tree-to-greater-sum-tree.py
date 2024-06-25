# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node, curr_sum):
            if not node:
                return
            dfs(node.right, curr_sum)
            curr_sum[0] += node.val
            node.val = curr_sum[0]
            dfs(node.left, curr_sum)

        curr_sum = [0]
        dfs(root, curr_sum)
        return root