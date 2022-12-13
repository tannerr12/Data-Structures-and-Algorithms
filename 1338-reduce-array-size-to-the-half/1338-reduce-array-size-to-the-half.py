class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        h = Counter(arr)
        
        a = []
        for key,val in h.items():
            a.append(val)
            
        a.sort(reverse=True)
    
        size = len(arr)
        res = 0
        c = 0
        while size > len(arr) //2:
            
            res +=1
            size -= a[c]
            c+=1
        
        
        return res
            
        