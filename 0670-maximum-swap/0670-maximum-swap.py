class Solution:
    def maximumSwap(self, num: int) -> int:
        
        c = Counter(str(num))
        snum = str(num)
        #print(c)
        ans = -1
        for j,val in enumerate(str(num)):
            
            for i in range(9,int(val),-1):
                if c[str(i)] > 0:
                    ans = [j,str(i)]     
                    break
            
            c[val] -= 1
            if ans != -1:
                break
        #print(ans)
        
        if ans == -1:
            return num
        res = []
        last = 0
        for i,val in enumerate(str(num)):
            if val == ans[1]:
                last = i
            res.append(val)
            
        
        res[ans[0]], res[last] = res[last], res[ans[0]]
        
        return int(''.join(res))
        
        
                