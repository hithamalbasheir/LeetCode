# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        #BFS with a queue, check every row and append the max in result, should be this trivial
        if not root:
            return []
        res = []
        q = [root]
        while q:
            n = len(q)
            curr_max = q[0].val
            for i in range(len(q)):
                curr = q.pop(0)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                curr_max = max(curr_max, curr.val)
            res.append(curr_max)
        return res

        