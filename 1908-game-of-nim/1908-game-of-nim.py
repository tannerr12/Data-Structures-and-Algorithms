class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        
       
        memo = {}
        def backtrack(piles):
            

            key = "-".join(map(str, piles))

            # Have we come across this state already?
            if key in memo:
                return memo[key]
            for j in range(len(piles)):
                
                for k in range(1,piles[j]+1):
                    noneSeen = False
                    piles[j] -= k
                    # order of pile heights.
                    next_state = sorted(piles)
                    if not backtrack(next_state):
                        memo[key] = True
                        return True           
                    piles[j] += k
            

            memo[key] = False
            return False
        
        
        return backtrack(piles)
            
            