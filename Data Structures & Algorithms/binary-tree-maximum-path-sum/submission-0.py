# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.out = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)

            print(node.val,l,r)

            leftcount =  node.val + l 
            rightcount  = node.val + r

          

            self.out = max(self.out,l+r+node.val) 
            return max(0,leftcount,rightcount)
           
            
        dfs(root)
        

        return self.out
        