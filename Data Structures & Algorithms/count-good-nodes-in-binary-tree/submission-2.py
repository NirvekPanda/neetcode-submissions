# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # store highest node so far, if curr > prev_high, total+1
        def dfs(node, high):
            if not node:
                return 0

            total = 0
            if node.val >= high:
                total = 1

            high = max(high, node.val)

            total += dfs(node.left, high)
            total += dfs(node.right, high)

            return total

        return dfs(root, root.val)
