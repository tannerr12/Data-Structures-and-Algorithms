class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        #locate the initial label
        
        level = 0
        while 2 ** level <= label:
            level += 1
        
        level -= 1
        
        #print(2 ** level)
        #print(level)
        
        pos = 0
        diff = label - (2 ** level)
        if level % 2:
            pos = (2 ** level) -1
            pos -= diff
        else:
            pos = 0
            pos += diff
            
        
        #print(pos)
        pos //= 2
        path = [label]
        while level > 0:
            level -= 1
            val = 0
            if level % 2:
                val = (2 ** (level + 1)) -1 - pos 
            else:
                val = (2 ** level) + pos
                
            path.append(val)
            pos //= 2
        
        path = path[::-1]
        return path
            
        
        