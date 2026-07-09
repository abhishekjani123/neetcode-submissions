# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Approach: DFS with Recursion
        Steps:
        1) Edge Condition:
           Whether Tree is empty or not, if true -> None
        2) Creating tmp and storing node left child
        3) Assigning left child with right child value
        4)right child -> tmp
        5)Recursive Call:
           1) Recursive call for left child
           2) Recursive call for right child
        T.C: O(n) , S.C: O(n)'''

        if root is None:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp


        self.invertTree(root.left)
        self.invertTree(root.right)
        return root



    