# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root)


    
    def validate(self, root, minVal=float('-inf'), maxVal=float('inf')):

        if root is None:
            return True

        if not (minVal < root.val < maxVal):
            return False
        
        return self.validate(root.left, minVal, root.val) and self.validate(root.right, root.val, maxVal)




        
