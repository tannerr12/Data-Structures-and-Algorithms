# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        arrL = []
        arrR  = []
        
        
        dhead = head
        
        while dhead:
            
            if dhead.val < x:
                arrL.append(dhead)
            else:
                arrR.append(dhead)
                
            
            dhead = dhead.next
        
        
        for i in range(len(arrL) -1):
            node = arrL[i]
            
            node.next = arrL[i+1]
            
        for i in range(len(arrR) -1):
            node = arrR[i]
            
            node.next = arrR[i+1]
        
        if len(arrR) > 0:
            arrR[-1].next = None
            if len(arrL) > 0:
                arrL[-1].next = arrR[0]
                
        return arrL[0] if len(arrL) > 0 else head