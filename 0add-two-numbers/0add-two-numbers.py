# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
      
        front = ListNode(0)
        tfront = front
   
        carry = 0
        while l1 and l2:
            
            
            calc = l1.val + l2.val 
            if calc + carry > 9:
                calc = calc - 10
            front.val = (calc + carry) 
            if l1.val + l2.val + carry > 9:
                carry = 1
            else:
                carry = 0
            if l1.next and l2.next:
                front.next = ListNode()
                front = front.next
            l1 = l1.next
            l2 = l2.next
  
        
        while l1:
            front.next = ListNode()
            front = front.next   
            calc = l1.val + carry
            if calc > 9:
                calc = calc - 10
            front.val = (calc) 
            if l1.val + carry > 9:
                carry = 1
            else:
                carry =0
            
            l1 = l1.next
        while l2:
            front.next = ListNode()
            front = front.next   
            calc = l2.val + carry
            if calc > 9:
                calc = calc - 10
            front.val = (calc) 
            if l2.val + carry > 9:
                carry = 1
            else:
                carry =0
            
            l2 = l2.next
        
        if carry:
            front.next = ListNode(carry)
        return tfront