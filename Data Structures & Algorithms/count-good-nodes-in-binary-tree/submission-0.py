# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.good_nodes = 0

        def dfs(node, maxVal = float("-inf")):

            if not node:
                return
            
            if node.val >= maxVal:
                self.good_nodes += 1
                newMax = node.val
            else:
                newMax = maxVal
            
            dfs(node.left, newMax)
            dfs(node.right, newMax)
        
        dfs(root)
        return self.good_nodes
        