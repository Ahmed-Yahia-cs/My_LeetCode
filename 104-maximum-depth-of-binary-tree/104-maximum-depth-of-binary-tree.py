# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #base case
        if not root:
            return 0
        
        #calculate the max in the left subtree
        max_left = max(self.maxDepth(root.left) + 1, 1)
        
        #calculate the max in the right subtree
        max_right = max(self.maxDepth(root.right) + 1, 1)
        
        return max(max_left , max_right)
        