"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        # 1. Create a mapping of original nodes to their corresponding copied nodes.
        node_map = {}
        curr = head

        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next

        # 2. Iterate through the original list again to set the next and random pointers of the copied nodes.
        curr = head
        while curr:
            copied_node = node_map[curr]
            copied_node.next = node_map.get(curr.next)  # Use .get() to handle None case gracefully
            copied_node.random = node_map.get(curr.random) # Use .get() to handle None case gracefully
            curr = curr.next

        return node_map[head]
        