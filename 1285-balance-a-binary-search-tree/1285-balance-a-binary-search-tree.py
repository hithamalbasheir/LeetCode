# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def create_balanced_bst(inorder, start, end):
            if start > end:
                return None
            mid = start + (end - start) // 2
            
            left_subtree = create_balanced_bst(inorder, start, mid - 1)
            right_subtree = create_balanced_bst(inorder, mid + 1, end)

            node = TreeNode(inorder[mid], left_subtree, right_subtree)
            return node
        
        def dfs(node, inorder):
            if not node:
                return
            dfs(node.left, inorder)
            inorder.append(node.val)
            dfs(node.right, inorder)

        inorder = []
        dfs(root, inorder)
        return create_balanced_bst(inorder, 0, len(inorder) - 1)