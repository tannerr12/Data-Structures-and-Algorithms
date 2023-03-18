class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        
        mp = defaultdict(int)
        
       # for i in range(len(arrays)):
       #     mp[i] = Counter(arrays[i])
            
        #print(mp)
        res = []
        for i in range(len(arrays[0])):
            
            valid = True
            n = arrays[0][i]
            for j in range(1, len(arrays)):
                
                while mp[j] < len(arrays[j]) and arrays[j][mp[j]] < n:
                    mp[j] += 1
                if mp[j] >= len(arrays[j]) or arrays[j][mp[j]] != n:
                    valid = False
                    break
            
            if valid:
                res.append(n)
                
        return res
            
        """
        short = float('inf')
        mn = float('inf')
        for i in range(len(arrays)):
            short = min(short,len(arrays[i]))
            mn = min(max(arrays[i], mn))
        
        subseq = set()
        
        def findSubSeq(i,s,take):
            if len(s) > 0 and take <= short:
                subseq.add(s[:-1])
                
            if i >= len(arrays[0]) or take > short:
                return
            
            
            #add
            findSubSeq(i+1,s+str(arrays[0][i]) + ',', take +1)
            
            #dont add
            findSubSeq(i+1,s,take)
            
        
        findSubSeq(0,'',0)
        #print(short)
        print(subseq)
        
        """
        """
        res = []
        for val in subseq:
            
            arr = val.split(',')

            x = 0
            if len(arr) <= len(res):
                continue
            for i in range(1,len(arrays)):
                x = 0
                valid = False
                for j in range(len(arrays[i])):
                    if str(arrays[i][j]) == arr[x]:
                        x+=1
                        if x == len(arr):
                            valid = True
                            break
                
                if not valid:
                    break
                
            if valid:
                res = arr.copy()
        
        
        newRes = []
        
        for val in res:
            newRes.append(int(val))
        return newRes
        """