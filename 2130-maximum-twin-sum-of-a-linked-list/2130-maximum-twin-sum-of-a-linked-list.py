# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = 0
        n = 0
        dhead = head
        
        while dhead:
            dhead = dhead.next
            n+=1
        
        dhead = head 
        mid = 0
        
        while mid+1 < n // 2:
            dhead = dhead.next
            mid +=1
        
        
        nxt = dhead.next
        dhead.next = None
        prev = None
        dhead = nxt
        nxt = None
        #reverse the second half
        while dhead:
            nxt = dhead.next
            d = dhead
            dhead.next = prev
            prev = d
            dhead = nxt
        
        #print(prev)
        #print(head)
        #print(n)
        
        while head:
            res = max(res, head.val + prev.val)    
            head = head.next
            prev = prev.next
        
        
        
        return res