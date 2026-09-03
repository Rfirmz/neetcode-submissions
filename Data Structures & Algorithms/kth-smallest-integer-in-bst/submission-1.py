# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        desiredVal = None
        count = 0
        
        def findK(node):

            if node is None:
                return
            
            findK(node.left)

            nonlocal count
            count += 1
            if count == k:
                nonlocal desiredVal
                desiredVal = node.val

            findK(node.right)

        findK(root)
        return desiredVal
