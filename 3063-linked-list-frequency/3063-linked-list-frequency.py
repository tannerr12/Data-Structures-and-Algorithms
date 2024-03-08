# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = defaultdict(int)
        
        dhead=head
        
        while dhead:
            count[dhead.val] += 1
            dhead = dhead.next
            
        new = ListNode(0)
        tnew = new
        for key in count:
            new.next = ListNode(0)
            new = new.next
            new.val = count[key]

        
        
        return tnew.next