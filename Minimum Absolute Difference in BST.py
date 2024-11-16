# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []

        values = []
        differences = []

        def dfs(node: Optional[TreeNode]):
            if node:
                values.append(node.val)
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        values = sorted(values)

        if len(values) <= 1:
            return []
            
        for i in range(1, len(values)):
            differences.append(
                values[i] - values[i-1]
            )

        return min(differences)