class Solution:
    def maximumBeauty(self, flowers: List[int]) -> int:
        
        prefix = []
        prefix.append(0)
        
        for i in range(len(flowers)):
            if flowers[i] >= 0:
                prefix.append(flowers[i] + prefix[-1])
            else:
                prefix.append(prefix[-1])
        
        #gather first and last idx
        first = {}
        last = {}
        
        for i in range(len(flowers)):    
            if flowers[i] not in first:
                first[flowers[i]] = i
        
        
        for i in range(len(flowers) -1,-1,-1):
            if flowers[i] not in last:
                last[flowers[i]] = i
                
        
        res = float('-inf')
        for i in range(len(flowers)):
            if first[flowers[i]] != last[flowers[i]]:    
                res = max(res, prefix[last[flowers[i]]] - prefix[first[flowers[i]] + 1] + (flowers[i] * 2))
        
        return res
        