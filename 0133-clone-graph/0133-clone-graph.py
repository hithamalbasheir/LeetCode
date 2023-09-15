"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #Base case
        if not node:
            return node
        #BFS - iterate and fill
        q = deque([node])
        #Initaite a map with all nodes and the neighbors beside it
        clones = {node.val: Node(node.val, [])}
        while q:
            cur = q.popleft()
            cur_clone = clones[cur.val]

            for nbr in cur.neighbors:
                if nbr.val not in clones:
                    clones[nbr.val] = Node(nbr.val, [])
                    q.append(nbr)
            
                cur_clone.neighbors.append(clones[nbr.val])

        return clones[node.val]
        