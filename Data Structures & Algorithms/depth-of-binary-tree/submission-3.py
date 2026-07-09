# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        1) Recursive DFS : T.C O(n), S.C: O(h), Best case: O(logn) -> Balanced Tree, Worst Case: O(n)
        2) Iterative DFS : T.C: O(n), S.C: O(n)
        
        # Iterative DFS
        1) Define Stack [[Node, 1]] Node = Root node, 1 = Initial Depth
        2) res = 0
        3) We will run the while loop till stack is not empty
        4) pop the node and the depth
        5) If node is there:
            1) find the max between depth andres and update res
            2) append left child in stack and increase depth by 1
            3) append right child and increase depth by 1
        6) return res

        # Recursive DFS

        1) check the edge case of tree is empty or not
            if root is None:
                return 0
        2) left = function name(root.left)
        3) right = function name(root.right)
        4) maxdepth = 1 + max(left, right)
        5) return maxdepth
        
        # Recursive DFS
        max_Depth = 0
        if root is None:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            max_Depth = 1 + max(left, right)
        return max_Depth

        '''

        stack = [[root, 1]]
        res = 0

        while stack:
            node , depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
        

