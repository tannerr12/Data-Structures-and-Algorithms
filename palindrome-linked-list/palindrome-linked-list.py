# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        l = 0
        
        dhead = head
        
        while head:
            l+=1
            head = head.next
        
        if l == 1:
            return True
        mid = l // 2
        mid -=1
        head = dhead
        r = None
        while head and mid:
            
            head = head.next
            mid-=1
        
        if l % 2:
            r = head.next.next
            head.next.next = None
            head.next = None
        else:
            r = head.next
           
            head.next = None
        
        # reverse R
        
        prev = None
        tempr = r
        
        
        while r:
            
            nxt = r.next
            r.next = prev
            prev = r
            r = nxt
        
        l = dhead
        

        while l and prev:
            if l.val != prev.val:
                return False
            l = l.next
            prev = prev.next
        return True
        
            
        