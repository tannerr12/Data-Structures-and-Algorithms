# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        h = collections.defaultdict(int)
        
        dhead = head
        
        while dhead:
            
            h[dhead.val] += 1
            dhead = dhead.next
            
        
        dhead = ListNode(-101)
        dhead.next = head
        tdhead = dhead
        while dhead:
            
            thead = dhead.next
            while thead and h[thead.val] >= 2:
                thead = thead.next
            
            dhead.next = thead
            dhead = dhead.next
        
        return tdhead.next