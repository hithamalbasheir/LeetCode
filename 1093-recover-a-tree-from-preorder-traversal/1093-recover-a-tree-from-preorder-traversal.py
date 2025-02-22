# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def val_num(idx):
            curr = 0
            while idx < len(traversal) and traversal[idx] != '-':
                curr *= 10
                curr += int(traversal[idx])
                idx += 1
            return curr, idx
        curr_depth = 0
        root_val, idx = val_num(0)
        root = TreeNode(val = root_val)
        nodes = {}
        nodes[1] = root
        print(nodes)
        while idx < len(traversal):
            print(idx)
            while idx < len(traversal) and traversal[idx] == '-':
                curr_depth += 1
                idx += 1
            num, idx = val_num(idx)
            if nodes[curr_depth]:
                node = nodes[curr_depth]
                if node.left:
                    node.right = TreeNode(val = num)
                    nodes[curr_depth + 1] = node.right  
                else:
                    node.left = TreeNode(val = num)
                    nodes[curr_depth + 1] = node.left
            curr_depth = 0
        return root