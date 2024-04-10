class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        heapify(deck)
        ans = [0] * len(deck)

        start = 0

        for i in range(start,len(ans),2):
            ans[i] = heappop(deck)
        
        flip = False
        if ans[-1] == 0:
            flip = False
        else:
            flip = True
        while deck:
            
            
            for i in range(len(ans)):
                if ans[i] == 0:
                    if not flip:
                        ans[i] = heappop(deck)
                        flip = True
                    else:
                        flip = False
                        continue
            

            
            
            
               
   
        return ans
        