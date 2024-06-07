class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        q = deque(hand)
        h  = Counter(hand)
        t = collections.defaultdict(int)
        count = len(hand)
        while count > 0:
            temp = []
            
            start = q.popleft()
            while q and t[start] > 0:
                t[start] -=1
                start = q.popleft()
          
            ostart = start
            while len(temp) != groupSize: 
                
                if h[start] > 0:
                    
                    temp.append(start)
                    h[start] -= 1
                    if ostart != start:
                        t[start] +=1
                    start += 1
                    count -=1
                else:
                    return False
            
        return True  
          