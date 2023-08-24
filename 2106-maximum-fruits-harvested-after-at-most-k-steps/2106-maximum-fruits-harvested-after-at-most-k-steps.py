class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        
        
        #take all right
        #take all left
        #take first left + right
        #take first right + left
        
        
        q = deque()
        score = 0
        left, right = -1, float('inf')
        ls,rs = 0,0
        mx = 0
        
        prefix = []
        prefix.append(0)
        for i in range(len(fruits)):
            p,s = fruits[i]
            prefix.append(prefix[-1] + s)
            mx += s
            if p < startPos:
                left = i
                ls = s
            elif p > startPos and right == float('inf'):
                right = i
                rs = s
            elif p == startPos:
                score += s
        
        if left >= 0:
            q.append([k - abs(startPos - fruits[left][0]), False, left, -1, score + ls])
        if right != float('inf'):
            q.append([k - abs(startPos - fruits[right][0]), False, right, 1, score + rs])
        res = score
        seen = set()
        while q:
            
            for i in range(len(q)):
                
                steps,turn,i,direc,sc = q.popleft()
                if steps >= 0:
                    res = max(res, sc)
                
                if steps <= 0 or sc == mx or (steps, turn, i, direc, sc) in seen:
                    continue
                
                seen.add((steps, turn, i, direc, sc))
                #if turned calculate score we can get from going the full distance
                if i + (1 * direc) >= 0 and i + (1 * direc) < len(fruits):
                    q.append([steps - abs(fruits[i][0] - fruits[i + (1 * direc)][0]), turn, i + (1 * direc), direc, sc +  fruits[i + (1 * direc)][1]])
                #turn around
                if not turn:
                    if direc == 1 and left != -1:
                        idx = bisect_right(fruits, fruits[i][0] - steps, key = lambda x: x[0])
                        if idx == 0:
                            sc += prefix[left+1]
                        else:    
                            if fruits[idx-1][0] == fruits[i][0] - steps:
                                idx -=1
                            sc += max(0, prefix[left+1] - prefix[idx])
                        res = max(res, sc)
                        
                        #q.append([steps - abs(fruits[i][0] - fruits[left][0]),True, left, -1, sc + fruits[left][1]])
                    elif direc == -1 and right != float('inf'):
                        #keep going
                        idx = bisect_right(fruits, fruits[i][0] + steps, key = lambda x: x[0])
                        if idx == len(fruits):
                            sc += max(0, prefix[-1] - prefix[right])    
                        else:    
                            if fruits[idx][0] > fruits[i][0] + steps:
                                idx -=1
                            sc += max(0, prefix[idx+1] - prefix[right])
                        res = max(res, sc)
                        
                        #q.append([steps - abs(fruits[i][0] - fruits[right][0]),True, right, 1, sc + fruits[right][1]])

            
        return res