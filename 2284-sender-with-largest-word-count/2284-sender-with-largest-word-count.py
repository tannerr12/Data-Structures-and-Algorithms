class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        
        

        
        mp = defaultdict(int)
        mx = 0
        for m,s in zip(messages,senders):
            
            wCount = m.count(' ') +1
            
            mp[s] += wCount
            
        mx = max(mp.values())
        
        mxarr = []
        for k,v in mp.items():
            if v == mx:
                mxarr.append(k)
        
        
        mxarr.sort(reverse=True)
        
        return mxarr[0]
        


            
        
        