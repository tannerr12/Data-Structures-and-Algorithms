class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        
        
        mp = {1: [2, 4, 5, 8, 6], 2: [1,3,4,5,6,9,7], 3: [2,6,5,8,4], 4:[1,2,5,3,9,7,8], 5:[1,2,3,4,6,7,8,9], 6: [1,2,3,5,7,8,9], 7:[4,5,6,2,8], 8:[1,3,4,5,6,7,9], 9:[2,4,5,6,8]}
        
        
        res = 0
        
        
        def dfs(seq):
            nonlocal res
            
            if len(seq) >= m and len(seq) <= n:
                res +=1
            
            if len(seq) > n:
                return
        
            last = None
            if seq:
                last = seq[-1]
            for i in range(1,10):
                if str(i) in seq:
                    continue
                if not last:
                    dfs(str(i))
                
                else:
                    l = int(last)
                    if i == l:
                        continue
                    if i in mp[l]:
                        dfs(seq + str(i))
                    
                    else:
                        
                        if l == 1:
                            if i == 9:
                                if '5' in seq:
                                    dfs(seq + str(i))
                                else:
                                    continue
                            if i == 3:
                                if '2' in seq:
                                    dfs(seq + str(i))
                                else:
                                    continue
                            if i == 7:
                                if '4' in seq:
                                    dfs(seq + str(i))
                                else:
                                    continue
                        elif l == 2:
                            
                            if i == 8:
                                if '5' in seq:
                                    dfs(seq + str(i))
                                else:
                                    continue
                        
                        elif l == 3:
                            if i == 9:
                                if '6' in seq:
                                    dfs(seq + str(i))
                                else:
                                    continue
                            if i == 1:
                                if '2' in seq:
                                    dfs(seq + str(i))
                                else:
                                    continue
                            if i == 7:
                                if '5' in seq:
                                    dfs(seq + str(i))
                                else:
                                    continue
                        elif l == 4:
                            if i == 6:
                                if '5' in seq:
                                    dfs(seq + str(i))
                                else:
                                    continue
               
                
                        elif l == 6:
                            if i == 4:
                                if '5' in seq:
                                    dfs(seq + str(i))
                                else:
                                    continue
                        elif l == 7:
                            if i == 1:
                                if '4' in seq:
                                    dfs(seq + str(i))
                                else:
                                    continue
                            if i == 3:
                                if '5' in seq:
                                    dfs(seq + str(i))
                                else:
                                    continue
                            if i == 9:
                                if '8' in seq:
                                    dfs(seq + str(i))
                                else:
                                    continue
                        elif l == 8:
                            if i == 2:
                                if '5' in seq:
                                    dfs(seq + str(i))
                                else:
                                    continue
                        
                        elif l == 9:
                            if i == 1:
                                if '5' in seq:
                                    dfs(seq + str(i))
                                else:
                                    continue
                            if i == 3:
                                if '6' in seq:
                                    dfs(seq + str(i))
                                else:
                                    continue
                            if i == 7:
                                if '8' in seq:
                                    dfs(seq + str(i))
                                else:
                                    continue
        
        dfs('')
        return res