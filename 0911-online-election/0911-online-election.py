class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        
        self.persons = persons
        self.times = times
        
        self.prefixW = []
        winner = 0
        count = 0
        h = defaultdict(int)
        #majority element
        for p,t in zip(persons,times):
            
            h[p] +=1
            if h[p] > count:
                winner = p
                count = h[p]
            
            elif h[p] == count:
                winner = p
                
            self.prefixW.append(winner)
    
            
            
        
        print(self.prefixW)

    def q(self, t: int) -> int:
        l = self.binarySearch(t)

        res = 0
        if self.prefixW[l] != None:
            return self.prefixW[l]
        else:
            return self.persons[l]
        
    
    
    
    def binarySearch(self,t):
        
        l = 0
        r = len(self.times) -1
        
        while l <= r:
            
            curr = (l+r) //2
            ti = self.times[curr]
            
            if ti > t:
                r = curr -1
            else:
                l = curr +1
        
        
        return l - 1 if l != 0 else 0
            

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)