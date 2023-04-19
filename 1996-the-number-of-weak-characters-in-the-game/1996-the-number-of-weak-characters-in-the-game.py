class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:

        
        properties.sort()
        res = 0
        
        mxdef = properties[-1][1]
        lastAtt = properties[-1][0]
        localdef = mxdef
        for i in range(len(properties)-2,-1,-1):
            att,deff = properties[i]
            if att != properties[i+1][0]:
                mxdef = max(localdef, mxdef)
                lastAtt = properties[i+1][0]
                
            localdef = max(localdef, deff)
            if att < lastAtt and deff < mxdef:
                res +=1
            
                
        return res
            
            
            
            
        
        
        