# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        first = None
        last = None
        mn = float('inf')
        idx = 0
        prev = None
        while head:
            
            
            if prev and head.next and ((prev.val > head.val and head.next.val > head.val) or (prev.val < head.val and head.next.val < head.val)):
                
                if first is None:
                    first = idx
                else:
                    mn = min(mn, idx - last)
                last = idx
            
        
            prev = head
            head = head.next
            idx +=1 
        
        
        if not first or first == last:
            return [-1,-1]
        
        mx = last - first
        
        return [mn,mx]