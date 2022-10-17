# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        
        dhead = head
        
        while dhead:
            
            thead = dhead
            while thead and thead.next and thead.val == thead.next.val:
                thead = thead.next
            
            
            dhead.next = thead.next
            dhead = dhead.next
            
            
        
        
        return head