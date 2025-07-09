# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r,s=[],[]
        while root or s:
            if root:
                r.append(root.val)
                s.append(root.right)
                root=root.left
            else:
                root=s.pop()
        return r