from sortedcontainers import SortedList
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        
        #keep track of the most used server
        score = defaultdict(int)
        
        #keep track of busy servers
        heap = []
        
        #maintain the status of the servers
        busy = SortedList([i for i in range(k)])
        
        for i in range(len(arrival)):
            
            at  = arrival[i]
            ld = load[i]
            
            #if the servers are done set them back to available
            while heap and heap[0][0] <= at:
                _,s = heappop(heap)
                busy.add(s)        
                
            #no servers are available
            if len(busy) == 0:
                continue
                
            #find the next best server to use
            find = i % k
            idxr = bisect_left(busy, find)
            
            #the server requested is available
            if idxr < len(busy) and busy[idxr] == find:
                heappush(heap, [at + ld, i % k])
                score[i % k] += 1
                busy.pop(idxr)
                
            #a server to the right is available
            elif idxr < len(busy):
                heappush(heap, [at + ld, busy[idxr]])  
                score[busy[idxr]] += 1
                busy.pop(idxr)
            #any server is available
            else:
                heappush(heap, [at + ld, busy[0]])  
                score[busy[0]] += 1
                busy.pop(0)
              
            
        

        #gather best servers
        ans = []
        mx = max(score.values())
        for key,val in score.items():
            if val == mx:
                ans.append(key)
                
        
        return ans
        