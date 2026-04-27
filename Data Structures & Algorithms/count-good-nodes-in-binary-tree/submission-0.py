# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0

        stack = [[root, root.val]] 
        ans = 0

        while stack:

            node,cmax = stack.pop()

            if node.val >= cmax:
                ans+=1
                cmax = node.val
            
            if node:
                if node.right:
                    stack.append([node.right,cmax])
                if node.left:
                    stack.append([node.left,cmax])

        return ans
        