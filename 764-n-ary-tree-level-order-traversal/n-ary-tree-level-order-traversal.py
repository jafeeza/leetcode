"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        res=[]
        q=deque()
        q.append(root)
        while q:
            qlen=len(q)
            level=[]
            for _ in range(qlen):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.extend(node.children)
            res.append(level)
        return res

            
