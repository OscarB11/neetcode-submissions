# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # reverse l1 + l2 
        # create string then convert to int then back to string 
        # Create final linked list 


        dummy = None
        prev = dummy
        curr = l1

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        newl1 = prev


        dummy2 = None
        prev2 = dummy
        curr2 = l2
  

        while curr2:
            nxt = curr2.next
            curr2.next = prev2
            prev2 = curr2
            curr2 = nxt
        
        newl2 = prev2

        s1= ""
        while newl1:
            s1 += str(newl1.val)
            newl1 = newl1.next
        
        s2= ""
        while newl2:
            s2 += str(newl2.val)
            newl2 = newl2.next

        print(s1,s2)
        ans = int(s1) + int(s2)
        print(ans)
        s3 = str(ans)
        
        # create result linked list in reverse order
        dummy = ListNode(0)
        current = dummy
        for ch in reversed(s3):
            current.next = ListNode(int(ch))
            current = current.next
        
        return dummy.next



        

          



        