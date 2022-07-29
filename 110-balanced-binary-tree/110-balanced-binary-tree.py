# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = self._validateBalance(root)[0]
        return balanced
        
    def _validateBalance(self, root: Optional[TreeNode]):
        
        if not root:
            return(True, 0)
        
        left, right = self._validateBalance(root.left), self._validateBalance(root.right)
        branches_balance = left[0] and right[0] 
        height_equlity = abs (left[1] - right[1]) <= 1
        return (branches_balance and height_equlity , max(left[1], right[1]) + 1)
        