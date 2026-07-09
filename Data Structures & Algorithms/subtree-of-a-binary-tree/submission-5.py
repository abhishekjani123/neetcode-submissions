# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subroot:
            return True
        if self.sametree(root, subroot):
            return True
        return (self.isSubtree(root.left,subroot) or self.isSubtree(root.right, subroot))

    def sametree(self, p, q):
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            return (self.sametree(p.left,q.left) and self.sametree(p.right, q.right))
        return False