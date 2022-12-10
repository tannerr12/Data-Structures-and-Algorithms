# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        dummy = ListNode(-1)
        dummy.next = head
        prev,start = dummy,head
        
        
        while start and start.next:
            
            #next set 
            nset = start.next.next
            first = start
            second = start.next
            
            
            second.next = start
            first.next = nset
            prev.next = second
            
            prev = first
            
            start = nset
        
        
        return dummy.next
            
            
            
        