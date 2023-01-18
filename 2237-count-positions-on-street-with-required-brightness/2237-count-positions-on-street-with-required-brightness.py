class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        
        
        arr = [0] * n
        
        for x,y in lights:
            
            start = max(x - y,0)
            end = (x + y) + 1
            
            
            arr[start] +=1
            if end <= n-1:
                arr[end] -=1
        
       
        total =0
        res = 0
        for i in range(n):
            
            total += arr[i]
            
            if total >= requirement[i]:
                res +=1
        
        
        return res