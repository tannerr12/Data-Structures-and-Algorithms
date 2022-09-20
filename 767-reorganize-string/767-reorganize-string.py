class Solution:
    def reorganizeString(self, s: str) -> str:
        h = Counter(s)
        arr = []
        
        for key,val in h.items():
            arr.append((val*-1,key))
            
        heapq.heapify(arr)
        
        result = ''
        prev = ''
        stack = []
        while arr:
            if arr[0][1] == prev and len(arr) ==1:
                return ''
            num,char = 0,'a'
            while True and arr: 
                num,char = heapq.heappop(arr)
                if char != prev:
                    break
                else:
                    stack.append((num,char))
            result+= char
            
            prev = char
            
            
            if num+1 != 0:
                heapq.heappush(arr,(num +1,char))
            
            while stack:
                heapq.heappush(arr,stack.pop())
                
        return result
            
            