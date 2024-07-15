# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = set()
        roots = {}
        for par, child, is_left in descriptions:
            children.add(child)
            if par not in roots:
                node = TreeNode(val = par)
                roots[par] = node
            if child not in roots:
                roots[child] = TreeNode(val = child)
            if is_left:
                roots[par].left = roots[child]
            else:
                roots[par].right = roots[child]
        for root in roots.keys():
            if root not in children:
                return roots[root]
        return None