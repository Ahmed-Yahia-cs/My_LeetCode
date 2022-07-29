# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def goodCount(root: TreeNode , max_value: int) -> int:
            
            if not root:
                return 0
            
            count = 1 if root.val >= max_value else 0
            max_value = max(root.val , max_value)
            
            count += goodCount(root.left , max_value)
            count += goodCount(root.right , max_value)
            
            return count
        
        return goodCount(root , root.val)
        