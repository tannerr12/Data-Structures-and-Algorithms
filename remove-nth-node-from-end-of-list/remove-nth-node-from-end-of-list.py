# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        headPointer = head
        thead = head
        count = 0
        while head:
            
            head = head.next
            count += 1
        
        
        if count == 1 and n == 1:
            return None
        if n == count:
            return thead.next
        while thead:
            
            
            if count == n +1:
   
                
                temp = thead.next.next
                thead.next.next = thead
                thead.next = temp
                
                
            thead = thead.next
            count -= 1
        
        
        
        return headPointer
        