# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r,s=[],[]
        curr=root
        while curr or s:
            while curr:
                s.append(curr)
                curr=curr.left
            curr=s.pop()
            r.append(curr.val)
            curr=curr.right
        return r