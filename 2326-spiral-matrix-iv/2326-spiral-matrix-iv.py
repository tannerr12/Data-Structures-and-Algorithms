# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        
        dp = [[-1 for j in range(n)] for i in range(m)]
        
        #print(dp)
        row = 0
        i,j = 0,0
        while head:
            j = row
            i = row
            while j < len(dp[0]) - row and head:
                dp[i][j] = head.val
                head = head.next
                j+=1

            j-=1
            i+=1
            while i < len(dp) - row and head:
                dp[i][j] = head.val
                head = head.next
                i+=1

            i-=1
            j -=1
            while j >= 0 + row and head:
                dp[i][j] = head.val
                head = head.next
                j -=1

            j = row
            i -=1
            while i >= 0 + row +1 and head:
            
                dp[i][j] = head.val
                head = head.next
                i-=1
            i+=1
            row +=1
        
        return dp
        