# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Sequential BFS in both trees till there's a difference, or I have finished and can return
        if not p and not q:
            return True
    
        pq, qq = deque([p]), deque([q])
        
        while pq and qq:
            pn, qn = pq.popleft(), qq.popleft()

            if not pn or not qn or pn.val != qn.val:
                return False
            if pn.left or qn.left:
                pq.append(pn.left)
                qq.append(qn.left)
            if pn.right or qn.right:
                pq.append(pn.right)
                qq.append(qn.right)
        return True
                