class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for i in range(len(cuboids)):
            w,l,h = cuboids[i]
            cuboids[i] = [w*l*h, w,l,h]
        
        cuboids.sort(reverse=True)
        
        @cache
        def dfs(i, width, length, height):
            
            if i >= len(cuboids):
                return 0
            
            
            area, w, l, h = cuboids[i]
            res = 0
            
            #skip this block
            res = max(res, dfs(i+1, width,length,height))
            
            # Attempt all 6 rotations
            if w <= width and l <= length and h <= height:
                res = max(res, h + dfs(i + 1, w, l, h))

            if w <= width and h <= length and l <= height:
                res = max(res, l + dfs(i + 1, w, h, l))

            if l <= width and h <= length and w <= height:
                res = max(res, w + dfs(i + 1, l, h, w))

            if l <= width and w <= length and h <= height:
                res = max(res, h + dfs(i + 1, l, w, h))

            if h <= width and w <= length and l <= height:
                res = max(res, l + dfs(i + 1, h, w, l))

            if h <= width and l <= length and w <= height:
                res = max(res, w + dfs(i + 1, h, l, w))
                
            return res
        
        
        return dfs(0,float('inf'), float('inf'), float('inf'))
        
        
            