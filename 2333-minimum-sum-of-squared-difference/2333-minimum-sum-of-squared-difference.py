class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        
        arr = []
        x = 0
        s = k1 + k2
        h = {}
        for i,j in zip(nums1,nums2):
            
         #   arr.append(abs(i-j))
            if abs(i-j) in h:
                h[abs(i-j)] +=1
            else:
                h[abs(i-j)] =1
            
            x+=1
        
        #print(arr)  
        #arr.sort(reverse = True)
        for key, val in h.items():
            heappush(arr, [-key, val])
        
       
        while arr and s:
            
            k,v = heappop(arr)
            k = -k
            k2,v2 = 0,0
            if arr:
                k2, v2 = heappop(arr)
                k2 = -k2
            gap = k - k2
            
            mx = gap * v
            
            if s >= mx:
                s-= mx
                if k2 > 0:
                    heappush(arr,[-k2, v2 + v])
            else:
                if k2 > 0:
                    heappush(arr,[-k2,v2])

                #t = mx - s
                
                div = s // v
                if s > v:
                    mod = s % v
                else:
                    mod = s
                
                if mod > 0:
                    heappush(arr, [-(k - (div+1)), mod])
                    
                heappush(arr, [-(k-div),v-mod])
                s= 0
        
        res =0
        while arr:
            k,v = heappop(arr)
            k = -k
            for i in range(v):
                res += k*k
            
        
        return res
            