# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        l1 = 0
        l2 = 0
        dhead1 = headA
        dhead2 = headB
        
        while headA:
            l1 +=1
            headA = headA.next
        
        while headB:
            l2+=1
            headB = headB.next
        
        headA = dhead1
        headB = dhead2
        while l2 > l1:
            l2-=1
            headB = headB.next
        
        while l1 > l2:
            l1 -=1
            headA = headA.next
        
        while headA and headB:
            if headA == headB:
                return headA
            
            headA = headA.next
            headB = headB.next
        
        
        return None
        
            