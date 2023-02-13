# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        dhead = head 
        
        
        odd = None
        even = None
        beg = dhead.next
        oddS = dhead
        i = 1
        while dhead:
            
            
            if dhead and i % 2 == 0:
                if not even:
                    even = dhead
                else:
                    even.next = dhead
                    even = even.next
                
                
            
            elif dhead and i % 2 == 1:
                if not odd:
                    odd = dhead  
                else:
                    odd.next = dhead
                    odd = odd.next
                
                
          
            i +=1
            dhead = dhead.next
        odd.next = beg
        even.next = None
        return oddS