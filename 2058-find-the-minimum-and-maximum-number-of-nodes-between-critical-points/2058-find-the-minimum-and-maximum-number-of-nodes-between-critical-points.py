# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        criticalPoints = []
        mn = float('inf')
        idx = 0
        prev = None
        while head:
            
            
            if prev and head.next and ((prev.val > head.val and head.next.val > head.val) or (prev.val < head.val and head.next.val < head.val)):
                criticalPoints.append(idx)
                if len(criticalPoints) > 1:
                    mn = min(mn, criticalPoints[-1] - criticalPoints[-2])
            
            
       
            prev = head
            
            
            head = head.next
            idx +=1 
        
        
        if len(criticalPoints) < 2:
            return [-1,-1]
        
        mx = criticalPoints[-1] - criticalPoints[0]
        
        return [mn,mx]