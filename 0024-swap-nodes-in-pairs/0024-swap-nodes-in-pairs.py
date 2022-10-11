# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dhead = head
        if head and head.next:
            head = head.next
        
        
        
        front = []
        start = True
        
        while dhead:
                
                front.append((dhead.next, dhead))
                tnext = dhead.next
                td = dhead
                dhead.next = None
                dhead = tnext
                if dhead is None:
                    break
                snxt = dhead.next
                dhead.next = td
                dhead = snxt
                


        #print(front)
        
        for i in range(len(front)-1):
            
            if front[i+1][0]:
                front[i][1].next = front[i+1][0]
            else:
                front[i][1].next = front[i+1][1]
            
        
        return head