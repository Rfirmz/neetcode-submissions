# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        """
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
        """

        # what I can do differently next time is just get the max within the 
        # function

        def dfs(node, maxVal):
            if not node:
                return 0
            good = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            return good + dfs(node.left, maxVal) + dfs(node.right, maxVal)

        return dfs(root, root.val)
            