# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque

        if not root:
            return []

        result = []
        queue = deque([root])  # Initialize a queue with the root node

        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()  # Dequeue the next node
                current_level.append(node.val)  # Add its value to the current level's list

                if node.left:
                    queue.append(node.left)  # Enqueue the left child
                if node.right:
                    queue.append(node.right)  # Enqueue the right child

            result.append(current_level)  # Add the current level's list to the result

        return result
