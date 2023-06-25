class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        
        row = defaultdict(list)
        col = defaultdict(list)
        mines.sort()
        idx = 0
        for i in range(n):
            for j in range(n):
                
                if idx < len(mines) and [i,j] == mines[idx]:
                    if len(row[i]) == 0:
                        row[i].append(0)
                        row[i].append(0)
                    else:
                        row[i].append(row[i][-1] + 0)
                    if len(col[j]) == 0:
                        col[j].append(0)
                        col[j].append(0)
                    else:    
                        col[j].append(col[j][-1] + 0)
                
                    idx +=1
                else:
                    if len(row[i]) == 0:
                        row[i].append(0)
                        row[i].append(1)
                    else:
                        row[i].append(row[i][-1] + 1)
                    if len(col[j]) == 0:
                        col[j].append(0)
                        col[j].append(1)
                    else:    
                        col[j].append(col[j][-1] + 1)
        
        
        def isGood(target):
            
            for i in range(target-1, n-target+1):
                for j in range(target-1, n-target+1):
                    
                    #check 4 prefix
                    up = abs(col[j][i+1] - col[j][(i+1)-target]) == target
                    down = abs(col[j][i] - col[j][i+target]) == target
                    left = abs(row[i][j+1] - row[i][(j+1)-target]) == target
                    right = abs(row[i][j] - row[i][j+target]) == target
                    
                    if up and down and left and right:
                        return True
                    
            
            return False
        
        l,r = 1, math.ceil(n/2)
        res = 0
        while l <= r:
            
            mid = (l + r) // 2
            
            if isGood(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
                
        
        return res
                