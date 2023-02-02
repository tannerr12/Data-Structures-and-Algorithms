class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        
        
        l = 0
        res = 0
        curr = 0
        for i in range(len(arr)):
            
            curr += arr[i]
            
            while i - l + 1 > k:
                
                curr -= arr[l]
                l +=1
            
            
            if i-l+1 == k and curr / k >= threshold:
                res +=1
        
        return res
            
            
        