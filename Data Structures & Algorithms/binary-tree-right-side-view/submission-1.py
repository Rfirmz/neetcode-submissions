# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        ret_list = list()
        dq = deque()
        dq.append(root)

        while dq:
            level = len(dq)
            for i in range(level):
                node = dq.popleft()

                if i == level - 1:
                    ret_list.append(node.val)
                
                if node.left:
                    dq.append(node.left)
                
                if node.right:
                    dq.append(node.right)
        
        return ret_list



        