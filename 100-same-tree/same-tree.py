# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        U:p and q are two trees I need return true both the trees same, like same values and False if it's not.
        P:
        Going for BFS, checking the root value and the children values like 
        p.left==q.left and p.right==q.right
        I:
        EC: both of roots empty, return True
            one of the tree present and the other return False
            the checking the values of children by traversing through the function
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            return isSameTree(self,p.left,q.left) and isSameTree(self,p.right,q.right)
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val!=q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

        