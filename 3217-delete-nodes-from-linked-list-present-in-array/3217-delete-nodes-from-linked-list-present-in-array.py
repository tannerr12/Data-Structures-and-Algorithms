# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        s = set(nums)
        
        while head and head.val in s:
            head = head.next
            
        
        
        dhead = head

        while head:
            
            nxt = head.next
            while nxt and nxt.val in s:
                nxt = nxt.next
            
            head.next = nxt
            head = head.next
        
        return dhead