# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head
        arr = []
        while head:
            arr.append((head.val, head))
            head = head.next
            

        arr =sorted(arr, key=lambda x : x[0])
        
        for i in range(len(arr) -1):
            arr[i][1].next = arr[i+1][1]
        
        
        
        arr[-1][1].next = None
        
        
        return arr[0][1]