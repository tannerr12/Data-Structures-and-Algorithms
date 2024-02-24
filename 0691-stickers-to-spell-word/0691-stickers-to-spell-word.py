class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        
        groups = defaultdict(lambda:defaultdict(int))
        gmask = defaultdict(int)
        
        t = [0] * 26
        for char in target:
            val = ord(char) - ord('a')
            t[val] += 1
            
        tmask = 0
        
        for val in target:
            v = ord(val) - ord('a')
            tmask |= (1 << v)
            
            
        for i in range(len(stickers)):    
            for char in stickers[i]:
                v = ord(char) - ord('a')
                if (tmask & (1 << v)) > 0:
                    gmask[i] |= (1 << v)
                    groups[i][v] += 1
        
       
        toRemove = set()
        for i in range(len(groups)):
            for j in range(len(groups)):
                if i == j or j in toRemove:
                    continue
                add = True
                for key, val in groups[i].items():
                    if val > groups[j][key]:
                        add = False
                        break
                
                if add:
                    toRemove.add(i)
                

        for i in range(len(groups)):
            if gmask[i] & tmask == 0:
                toRemove.add(i)
        
        #print(toRemove)
        
        for val in toRemove:
            if val in groups:
                del groups[val]
                del gmask[val]
        
        

        #print(t)
        
        @cache
        def dfs(t,bitmask):
            
            if bitmask == 0:
                return 0
            
            res = float('inf')
         
            #try each sticker 
            for i in groups:
                if gmask[i] & bitmask == 0:
                    continue
                
                bt = list(t)
                    
                #common_bitmask = gmask[i] & bitmask
     
                    
                tm = bitmask
                g = groups[i]
                for char_position in range(len(t)):
                    
                    
                    #lsb_position = common_bitmask & -common_bitmask  # Isolates the LSB
                    #char_position = (lsb_position.bit_length() - 1)  # Converts to character position
                    #key = chr(ord('a') + char_position)
                    if g[char_position] > 0 and bt[char_position] > 0:
                        bt[char_position] -= min(bt[char_position], g[char_position])
                        if bt[char_position] == 0:
                            tm ^= (1 << char_position)
                        
                    
                    #common_bitmask &= ~lsb_position
                res = min(res, dfs(tuple(bt), tm) + 1)
            
            return res
        
        ans = dfs(tuple(t),tmask)
        
        return ans if ans != float('inf') else -1
                    
                
                        
                        
        '''
        
                        while common_bitmask:
                    g = groups[i]
                    lsb_position = common_bitmask & -common_bitmask  # Isolates the LSB
                    char_position = (lsb_position.bit_length() - 1)  # Converts to character position
                    #key = chr(ord('a') + char_position)
                    if char_position in g:
                        bt[char_position] -= min(bt[char_position], g[char_position])
                        if bt[char_position] == 0:
                            del bt[char_position]
                            #val = ord(char_position) - ord('a')
                            tm ^= (1 << char_position)
                        
                    common_bitmask &= ~lsb_position
        '''     
        
        