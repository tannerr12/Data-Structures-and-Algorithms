class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        pep = people.copy()
        
        heapq.heapify(pep)
        
        h  = {}
        res = []
        temp = []
        #addedKeys = set()
        while pep:
            
            height, p = heapq.heappop(pep)
            if height not in h:
                h[height] = 0
            if h[height] != p:
                temp.append([height,p])
            
            else:
                res.append([height,p])
               #addedKeys.add(height)
                
                for key in h:
                    if key <= height:
                        h[key] +=1
                        
                
                while temp:

                    x,y = temp.pop()
                    heapq.heappush(pep,[x,y])
        return res
        