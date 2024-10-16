class Solution:
    def countBlackBlocks(self, m: int, n: int, co: List[List[int]]) -> List[int]:
        
        s = set()
        
        for x,y in co:
            s.add((x,y))
            
        
        
        arr = [0] * 5
        
        total = (m-1) * (n-1)
        def scan(i,j):
            nonlocal total
            count = 0
            count += (i,j) in s
            count += (i+1,j) in s
            count += (i,j+1) in s
            count += (i+1,j+1) in s
            
            total -=1
            arr[count] += 1
            
        
        for x,y in co:
            
            if x > 0 and y != n-1 and (x-1,y) not in s:
                scan(x-1,y)
            if y > 0 and x != m-1 and (x, y-1) not in s and (x+1,y-1) not in s:
                scan(x,y-1)
            
            if y > 0 and x > 0 and (x-1, y-1) not in s and (x,y-1) not in s and (x-1,y) not in s:
                scan(x-1,y-1)
            if x != m-1 and y != n-1:
                scan(x,y)

        
        arr[0] = total
        return arr
        