"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        dhead = head
        
        
        
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        
        mn = float('inf')
        mx = 0
        while head:
            mn = min(mn,head.val)
            mx = max(mx,head.val)
            head = head.next
            if head == dhead:
                break
        

        while head:
            
            
            if mn == mx or (head.next.val == mn and insertVal >= head.val and head.val == mx) or (head.next.val >= insertVal and head.val <= insertVal) or (insertVal < head.next.val and insertVal < head.val and head.next.val == mn and head.val == mx): 
                nxt = head.next
                head.next = Node(insertVal)
                head = head.next
                head.next = nxt
                return dhead
            
            head = head.next