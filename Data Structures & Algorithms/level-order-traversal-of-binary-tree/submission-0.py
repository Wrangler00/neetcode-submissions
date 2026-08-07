# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        sol = []
        level = 0
        bfs = deque([root])

        while bfs:
            sol.append([])
            size = len(bfs)
            while size > 0:
                node = bfs.popleft()
                sol[level].append(node.val)
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
                size -= 1
            level += 1

        return sol