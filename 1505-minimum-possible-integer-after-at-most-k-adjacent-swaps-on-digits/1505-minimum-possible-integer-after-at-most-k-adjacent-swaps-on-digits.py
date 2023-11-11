class Solution:
    def minInteger(self, num: str, k: int) -> str:
        
        c = [0] * (len(num) + 1)
        
        def update(x,val):
            
            while x < len(c):
                c[x] += val
                x += x & -x
            
        def get(x):
            
            res = 0
            
            while x:
                res += c[x]
                x -= x & -x
        
            
            return res
        
        for i in range(len(c)):
            update(i+1,1)
        
        
        mpq = [deque() for i in range(10)]
        res = []
        for i in range(len(num)):
            mpq[int(num[i])].append(i)
            res.append(num[i])
        #print(mpq)
        
        #print(res)
       
        pos = len(num) -1
        moved = set()
        add = []
        taken = set()
        j = 0
        while k > 0 and j < len(res):
            bestnum = float('inf')
            bestpos = float('inf')
            curpos = 0
            
            for i in range(10):
                if len(mpq[i]) == 0:
                    continue
                if  get(mpq[i][0]+1) -1 <= k or get(mpq[i][0]+1) -1 <= bestpos:
                    if (get(mpq[i][0]+1) -1 < bestpos and bestpos != k)  or bestnum > int(num[mpq[i][0]]):
                        bestpos = max(k, get(mpq[i][0]+1) -1)
                        bestnum = int(num[mpq[i][0]])
                        curpos = mpq[i][0]
            
            
            v = mpq[bestnum].popleft()
            
            if k - get(v+1) -1 <= 0:
                res[j + (bestpos - k)] = str(bestnum)
                taken.add(j + (bestpos - k))
            else:
                res[j]=(str(bestnum))
                taken.add(j)
                
            k -= get(v+1) -1
            update(v+1, -1)
            moved.add(v)
            
            j += 1
            
            '''
            cost = (get(idx + len(num)) - 1)
            if cost <= k:
                k -= cost
                res.append(val)
                #res[i] = val
                #i += 1
                update(idx + len(num), -1)
                moved.add(idx)
            '''



        
        j = 0
        for i in range(len(num)):
            while j in taken:
                j+=1
            
            if i not in moved:
                res[j] = num[i]
                j+=1
            
        #print(res)
         
        return ''.join(res)
      