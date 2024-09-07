# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root: return False
        def dfs(node, curr):
            if not curr: return True
            if not node or node.val != curr.val: return False
            return dfs(node.left, curr.next) or dfs(node.right, curr.next)
        
        if dfs(root, head):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)