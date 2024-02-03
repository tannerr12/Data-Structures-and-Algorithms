class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        
        start = 0
        #count = 0
        for i in range(len(cells)):
            if cells[i] > 0:
                start |= (1 << i)
            
         
        
        arr = []
        seen = set()
        
        while start not in seen:
            seen.add(start)
            arr.append(start)
            newstart = 0
            for i in range(1, 7):
                last = start & (1 << i-1) > 0
                nxt = start & (1 << i+1) > 0
                if last == nxt:
                    newstart |= (1 << i)
            
            start = newstart
         
        
        idx = 0
        while start != arr[idx]:
            idx +=1
        n -= idx
        arr = arr[idx:]
        #print(arr)
        
        ans = n % len(arr)
        a = [0] * 8
        for i in range(8):
            if arr[ans] & (1 << i) > 0:
                a[i] = 1
        return a