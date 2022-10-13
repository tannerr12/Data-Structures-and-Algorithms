# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
   
        
        dhead = head
        

        dhead = ListNode(-101)
        dhead.next = head
        tdhead = dhead
        while dhead:
            
            thead = dhead.next
            prev = -101
            while thead and (thead.next and thead.val == thead.next.val or thead.val == prev):
                prev = thead.val
                thead = thead.next
                
            
            dhead.next = thead
            dhead = dhead.next
        
        return tdhead.next