class Solution:
    def minimumDistance(self, word: str) -> int:
        
        dist = defaultdict(dict)
        
        for i in range(26):
            letter = chr(i + ord('A'))
            r,c = i // 6, i % 6 
            for j in range(26):
                nextLetter = chr(j + ord('A'))
                
                col = j % 6
                row = j // 6
                
                dist[letter][nextLetter] = abs(r - row) + abs(c - col)
        
        #print(dist)
        
        
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
                heappush(heap, (cost + dist[f1][word[idx]], word[idx], f2, idx + 1))
            else:
                heappush(heap, (cost, word[idx], f2, idx + 1))
            if f2 != '':
                #move finger2
                heappush(heap, (cost + dist[f2][word[idx]], f1, word[idx], idx + 1))
            else:
                heappush(heap, (cost, f1, word[idx], idx + 1))
        