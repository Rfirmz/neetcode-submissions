# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS algorithm
# visit nodes at each level first then their children

# queue can do this

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        dq = deque()
        dq.append(root)

        ret_list = list()
        # .popleft() to get the front

        while dq:

            n = len(dq)
            add = list()

            for _ in range(n):
                node = dq.popleft()
                add.append(node.val)

                if node.left:
                    dq.append(node.left)
                
                if node.right:
                    dq.append(node.right)
            
            ret_list.append(add)
        

        return ret_list

    

        

