class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        
        heapq.heapify(people)
        
        h  = {}
        res = []
        temp = []
     
        while people:
            
            height, p = heapq.heappop(people)
            if height not in h:
                h[height] = 0
            if h[height] != p:
                temp.append([height,p])
            
            else:
                res.append([height,p])
               
                
                for key in h:
                    if key <= height:
                        h[key] +=1
                        
                
                while temp:

                    x,y = temp.pop()
                    heapq.heappush(people,[x,y])
        return res
        