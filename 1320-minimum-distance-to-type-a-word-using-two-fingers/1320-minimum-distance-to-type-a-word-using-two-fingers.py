class Solution:
    def minimumDistance(self, word: str) -> int:
        
        
        def distance(x,y):
            r1,c1 = (ord(x) - ord('A')) // 6,(ord(x) - ord('A')) % 6
            r2,c2 = (ord(y) - ord('A')) // 6,(ord(y) - ord('A')) % 6
            return abs(r1 - r2) + abs(c1 - c2) 
            

        heap = []
        
        heappush(heap, (0, '', '', 0))
        seen = set()
        while heap:
            
            cost, f1, f2,idx = heappop(heap)
            if (f1,f2,idx) in seen or (f2,f1,idx) in seen:
                continue
            seen.add((f1, f2, idx))
            seen.add((f2, f1, idx))
            if idx == len(word):
                return cost
            
            if f1 != '':
                #move finger1
                heappush(heap, (cost + distance(f1,word[idx]), word[idx], f2, idx + 1))
            else:
                heappush(heap, (cost, word[idx], f2, idx + 1))
            if f2 != '':
                #move finger2
                heappush(heap, (cost + distance(f2,word[idx]), f1, word[idx], idx + 1))
            else:
                heappush(heap, (cost, f1, word[idx], idx + 1))
        