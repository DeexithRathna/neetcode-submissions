# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxHeight(node):
            if node is None:
                return 0
            left = maxHeight(node.left)
            right = maxHeight(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right) 
        
        height = maxHeight(root)
        return height != -1