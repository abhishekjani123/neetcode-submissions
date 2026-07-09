# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        Approach: Recursive DFS
        T.C: O(n) S.C: O(h)
        Steps:

        1) defining global variable res (self.res)
        2) creating function dfs(node)
        3) check if node is not empty, if yes return 0
        4) left = dfs(node.left)
        5) right = dfs(node.right)
        6) self.res = max(self.res, left+right)
        7) return 1 + max(left,right) -> Max height from that level
        8) outside of function call dfs(root)
        9) return res '''
        self.res = 0

        def dfs(node):
            if not node:
                return 0
            else:
                left = dfs(node.left)
                right = dfs(node.right)
                self.res = max(self.res, left+right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.res