class Solution:
    def similarRGB(self, color: str) -> str:
        
        
        def findTarget(color_selection):
            
            min_diff = 1000
            
            ans = -1
            
            
            for i in range(16):
                cur_diff = (int(color_selection, 16) - i * 17) **2
                
                if cur_diff < min_diff:
                    min_diff = cur_diff
                    ans = i
                    
                
                
            
            
            return hex(ans)[-1] * 2
    
    
        
        
        target_color = '#'
        
        
        for i in range(1,6,2):
            target_color += findTarget(color[i:i + 2])
            
        
        return target_color