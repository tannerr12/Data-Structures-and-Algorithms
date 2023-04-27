class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        '''
        parent = defaultdict(int)
        rank = defaultdict(int)
        
        def find(val):
            
            if parent[val] == val:
                return val
            
            parent[val] = find(parent[val])
            
            return parent[val]
        
        
        
        def union(x,y):
            
            v1,v2 = find(x),find(y)
            
        ''' 
        arr.sort()
        count = Counter(arr)

        for i in range(len(arr)):
            val = arr[i]
            
            if count[val] > 0 and count[val * 2] > 0:
                count[val] -=1
                count[val*2] -=1
        
        return max(count.values()) == 0