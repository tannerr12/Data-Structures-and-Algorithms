class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        
    
        
        mx = 0
        mn = float('inf')
        mean = 0
        median = -1
        '''
        count.sort()
        
        if len(count) % 2:
            median = count[len(count) //2]
        else:
            median = count[len(count) // 2] + count[(len(count) // 2) + 1] / 2
        '''
        mxCount = 0
        mode = 0
        c = defaultdict(int)
        total = sum(count)
        
        mid = total // 2
        current =0
        medcount = -1
        second = False
        for i in range(len(count)):
            val = count[i]
            if val > 0:
                mx = max(mx,i)
                mn = min(mn,i)
            mean += i * val
            
            if medcount != -1 and val > 0 and second == False:
                medcount += i
                second = True
                
            if val > mxCount:
                mxCount = max(mxCount,val)
                mode = i
            
            current += val 
            if current >= (mid + 1) and total % 2 and median == -1:
                median = i
            elif current > mid and total % 2 == 0 and median == -1 and medcount == -1:
                median = i
            elif current == mid and medcount == -1:
                medcount = i
        
        if median == -1:
            median = medcount / 2
        return [mn,mx,mean / total,median,mode]