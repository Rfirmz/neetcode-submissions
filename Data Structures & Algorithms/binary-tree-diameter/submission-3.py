# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        ret = 0

        def counter(node):
            nonlocal ret

            if not node:
                return 0
            
            left = counter(node.left)
            right = counter(node.right)

            ret = max(ret, left + right)

            return 1 + max(left, right)
            

        counter(root)
        return ret 