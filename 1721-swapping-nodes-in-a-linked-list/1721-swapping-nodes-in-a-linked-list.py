# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        size = 0
        
        dhead = head
        
        while dhead:
            
            dhead = dhead.next
            size+=1
            
      
        back = size - k + 1
        
        dhead = head
        frontN = None
        backN = None
        count = 0
        while dhead:
            count +=1
            if count == k:
                frontN = dhead
            
            if count == back:
                backN = dhead
            
            dhead = dhead.next
        
        
        frontN.val, backN.val = backN.val, frontN.val
        
        return head
            
           
            