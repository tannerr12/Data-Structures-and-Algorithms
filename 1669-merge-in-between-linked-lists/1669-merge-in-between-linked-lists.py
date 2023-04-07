# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        
        ath = None
        bth = None
        
        count = 0
        dhead = list1
        
        while dhead:
            if count == a-1:
                ath = dhead
            dhead = dhead.next
            if count == b:
                bth = dhead
            
            count +=1
        
        #print(ath.val)
        #print(bth.val)
        
        ath.next = list2
        
        dheadl2 = list2
        
        while dheadl2.next:    
            dheadl2 = dheadl2.next
        
        dheadl2.next = bth
        
        return list1