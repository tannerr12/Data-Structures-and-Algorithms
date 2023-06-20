class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        res = 0
        idx = 0
        for i in range(len(players)):
            
            while idx < len(trainers) and trainers[idx] < players[i]:
                idx +=1
            
            if idx < len(trainers) and trainers[idx] >= players[i]:
                res +=1
                idx+=1
            else:
                break
        
        return res