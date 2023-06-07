# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        
        s = set(nums)
        
        dhead = head
        res = 0
        curr = 0
        while dhead:
            
            if dhead.val in s:
                curr += 1
            else:
                if curr >= 1:
                    res +=1
                    curr = 0
            dhead = dhead.next
        
        
        return res + (curr > 0)