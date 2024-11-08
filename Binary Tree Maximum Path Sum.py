# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answer=float(-inf)
        
        def dfs(node):
            nonlocal answer

            if node==None:
                return 0
            
            leftsum=dfs(node.left)
            rightsum=dfs(node.right)
            
            leftsum=max(leftsum,0)
            rightsum=max(rightsum,0)
            
            answer=max(answer,node.val+leftsum+rightsum)
            
            return node.val+max(leftsum,rightsum)
        
        dfs(root)
        return answer