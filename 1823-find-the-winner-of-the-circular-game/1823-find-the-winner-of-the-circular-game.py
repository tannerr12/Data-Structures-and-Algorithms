from sortedcontainers import SortedList
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friend = 0
        count = n
        os = SortedList()
        for i in range(1,n+1):
            os.add(i)
        
        while count != 1:
            friend = (friend + (k -1)) % (count)
            count -=1
            os.pop(friend)
            
            
        
        return os[0]
        
            
            
            