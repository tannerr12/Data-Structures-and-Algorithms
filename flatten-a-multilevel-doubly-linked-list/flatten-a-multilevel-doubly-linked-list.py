"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        node = Node()
        dn = node
        stack = []
        
        while head:
            
            node.val = head.val
            node.next = Node(-1)
            n = node
            node = node.next
            node.prev = n
            
            if head.child:
                
                if head.next:
                    stack.append(head.next)
                head = head.child
            else:
                head = head.next
                if head == None and stack:
                    head = stack.pop()
        
        
        
        node.prev.next = None
        return dn
            