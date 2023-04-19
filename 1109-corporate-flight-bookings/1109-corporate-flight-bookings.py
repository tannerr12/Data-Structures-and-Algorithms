class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n
        arr = [0] * (n+1)
        for x,y,z in bookings:
            
            arr[x-1] += z
            arr[y] -= z
        

        running = 0
        for i in range(1, n + 1):
            
            running += arr[i-1]
            res[i-1] = running
        
        return res
            
            
                
            
            