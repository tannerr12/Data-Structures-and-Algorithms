# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        
        ans = 0
        
        while head:
            
            if head.val > head.next.val:
                ans += 1
            else:
                ans -= 1
            
            head = head.next.next
    
        if ans == 0:
            return "Tie"
        return "Even" if ans > 0 else "Odd"