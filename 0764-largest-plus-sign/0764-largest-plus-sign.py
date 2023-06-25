class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        
        col = defaultdict(list)
        row = defaultdict(list)
        mines.sort()
        idx = 0
        for i in range(n):
            for j in range(n):
                
                if idx < len(mines) and [i,j] == mines[idx]:
                    if len(col[i]) == 0:
                        col[i].append(0)
                        col[i].append(0)
                    else:
                        col[i].append(col[i][-1] + 0)
                    if len(row[j]) == 0:
                        row[j].append(0)
                        row[j].append(0)
                    else:    
                        row[j].append(row[j][-1] + 0)
                
                    idx +=1
                else:
                    if len(col[i]) == 0:
                        col[i].append(0)
                        col[i].append(1)
                    else:
                        col[i].append(col[i][-1] + 1)
                    if len(row[j]) == 0:
                        row[j].append(0)
                        row[j].append(1)
                    else:    
                        row[j].append(row[j][-1] + 1)
        
        #for i in row:    
        #    row[i].append(row[i][-1])
        #for j in col:
        #    col[j].append(col[j][-1])
        
        def isGood(target):
            
            for i in range(target-1, n-target+1):
                for j in range(target-1, n-target+1):
                    
                    #check 4 prefix
                    up = abs(row[j][i+1] - row[j][(i+1)-target]) == target
                    down = abs(row[j][i] - row[j][i+target]) == target
                    left = abs(col[i][j+1] - col[i][(j+1)-target]) == target
                    right = abs(col[i][j] - col[i][j+target]) == target
                    
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
                