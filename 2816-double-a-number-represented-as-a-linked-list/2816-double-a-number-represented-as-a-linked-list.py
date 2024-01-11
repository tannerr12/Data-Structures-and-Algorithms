# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        def reverse(node):
            
            prev = None
            
            while node:
                
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            
            
            
            return prev
        
        
        node = reverse(head)
        nodet = node
        carry = 0
        prev = None
        while node:
            val = node.val
            node.val = (node.val * 2 + carry) % 10
            
            if val * 2 + carry >= 10:
                carry = 1
            else:
                carry = 0
            
            prev = node
            node = node.next    
        
        if carry:
            node = ListNode(carry)
            prev.next = node
        
        
        node = reverse(nodet)
        
        return node