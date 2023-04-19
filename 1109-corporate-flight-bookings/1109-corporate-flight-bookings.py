class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        arr = []
        for x,y,z in bookings:
            
            arr.append([x, z])
            arr.append([y+1, -z])
        
        
        arr.sort()
        
        res = [0] * n
        idx = 0
        running = 0
        for i in range(1, n + 1):
            
            while idx < len(arr) and arr[idx][0] <= i:
                running += arr[idx][1]
                idx +=1
            
            res[i-1] = running
        
        return res
            
            
                
            
            