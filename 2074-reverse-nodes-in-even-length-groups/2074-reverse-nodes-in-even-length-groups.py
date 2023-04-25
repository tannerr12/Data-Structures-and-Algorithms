# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        dhead = head
        count = 1
        prev = None
        tcount = 0
        start = None
        last = None
     
        while head:

            if tcount == count:
                count +=1
                tcount = 0
                if count % 2 and start:
                    start.next = head
                    last.next = prev
                last = start
                start = None
                
                
            
            if count % 2 == 0:
                if not start:
                    last = prev
                    start = head
                    prev = head
                    nxt = head.next
                    head.next = None
                    head = nxt
                else:
                    nxt = head.next
                    head.next = prev
                    prev = head
                    head = nxt
            else:
                if not start:
                    #last = prev
                    start = head
                prev = head
                head = head.next
            tcount +=1
        
        
        
        
        if count % 2 == 0 and start and tcount % 2 == 0:
            start.next = head
            last.next = prev
        elif count % 2 == 0 and start and tcount % 2 and tcount > 1:
            #start.next = prev
            #last.next = head
                        
            head = prev
            count = 0
            while head:
                if count == 0:
                    prev = head
                    nxt = head.next
                    head.next = None
                    head = nxt
                    count +=1
                else:
                    nxt = head.next
                    head.next = prev
                    prev = head
                    head = nxt
                    
            #start.next = prev
            last.next = prev
            
        elif tcount % 2 == 0 and count % 2:
            
            head = start
            count = 0
            while head:
                if count == 0:
                    prev = head
                    nxt = head.next
                    head.next = None
                    head = nxt
                    count +=1
                else:
                    nxt = head.next
                    head.next = prev
                    prev = head
                    head = nxt
                    
            #start.next = prev
            last.next = prev
            
            
            
            

        return dhead