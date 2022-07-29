# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def toBST(l,r):
            
            if l > r :
                return None
            
            mid = (l + r) // 2
            b_tree = TreeNode(nums[mid])
            b_tree.left = toBST(l , mid - 1 )
            b_tree.right = toBST(mid + 1 , r)
            return b_tree 
        
        return toBST(0, len(nums) - 1)