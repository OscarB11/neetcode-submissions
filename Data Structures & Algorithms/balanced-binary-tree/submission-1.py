# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [True,0]

            lst = dfs(root.left)
            rst = dfs(root.right)
            if (lst[0] == True) and (rst[0] == True) and abs(lst[1] - rst[1]) <=1: 
                return [True,1+max(lst[1] ,rst[1])]
            else:
                return [False,1+max(lst[1] ,rst[1])]
        

        return dfs(root)[0]






        