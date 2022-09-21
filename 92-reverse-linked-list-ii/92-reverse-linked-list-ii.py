# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right:
            return head
        lnode,rnode = None,None
        ehead = None
        count =0
        
        h = head
        
        while h:
            count +=1
            temp = h.next
            if count == left-1:
                ehead = h
                h.next = None
            if count == right:
                h.next = None
            
            
            
            if count == left:
                lnode = h
            if count == right+1:
                rnode = h
            h = temp
                
        
        
        prev = None
        
        while lnode:
            
            temp = lnode.next
    
            lnode.next = prev
            prev = lnode
            lnode = temp
        
        if ehead:
            ehead.next = prev
        if rnode:    
            if left == 1:
                head = prev
            while prev.next:
                prev = prev.next


            prev.next = rnode
        
            return head
       
        
        return head if left > 1 else ehead if ehead else prev
        
        
        
            
        
   
        
        
            