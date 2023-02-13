# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        l = 0
        dhead = head
        
        while head:
            l +=1
            head = head.next
        
        
        start = k % l
        end = l - start
        head = dhead
        
        if start == 0:
            return head
        hend = dhead
        hstart = dhead 
        while end -1:
            hend = hend.next
            end -=1
        
        nxt = hend.next
        hend.next = None
        hend = nxt
        
        while hend.next:
            hend = hend.next
        
        hend.next = hstart
 
        return nxt
       