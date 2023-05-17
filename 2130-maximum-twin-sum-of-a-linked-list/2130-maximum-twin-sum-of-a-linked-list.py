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
        
        #get the size
        while dhead:
            dhead = dhead.next
            n+=1
        
        dhead = head 
        mid = 1
        
        #cut off the mid point
        while mid < n // 2:
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

        #find the maximum value
        while head:
            res = max(res, head.val + prev.val)    
            head = head.next
            prev = prev.next

        return res